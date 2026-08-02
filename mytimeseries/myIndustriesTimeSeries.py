"""myIndustriesTimeSeries.py."""

__title__: str = "myIndustriesTimeSeries"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import os
from typing import Optional
from mytuple import myTuple
from mydatabase import mySQLDataBase
from myfilebase import myFileBase
from mytimeseries import myIndustriesTimeSeriesDefinitions
from mytimeseries import myTableSQLIndustriesTimeSeries


@dataclasses.dataclass(init=False)
class MyIndustriesTimeSeries(mySQLDataBase.MySQLDataBase):
    """

    """
    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # SQL Table Static Watch List
    _my_table_sql_industries_time_series: myTableSQLIndustriesTimeSeries.MyTableSQLIndustriesTimeSeries = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLIndustriesTimeSeries.MyTableSQLIndustriesTimeSeries)))

    # tuple indices
    _int_industries_time_series_industries_name_column_index: int = dataclasses.field(repr=False, default=0)
    _int_industries_time_series_quote_numbers_column_index: int = dataclasses.field(repr=False, default=0)
    _int_industries_time_series_change_percent_column_index: int = dataclasses.field(repr=False, default=0)
    _int_industries_time_series_twenty_day_change_percent_json_array_column_index: int = dataclasses.field(repr=False, default=0)

    _str_industries_time_series_industries_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_industries_time_series_quote_numbers_column_name: str = dataclasses.field(repr=False, default='')
    _str_industries_time_series_change_percent_column_name: str = dataclasses.field(repr=False, default='')
    _str_industries_time_series_twenty_day_change_percent_json_array_column_name: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    _int_num_columns: int = dataclasses.field(repr=False, default=0)

    _list_industries_tuples: list[tuple[str, int]] = dataclasses.field(repr=False, default_factory=list)

    _list_change_percent_tuples: list[tuple] = dataclasses.field(repr=False, default_factory=list)

    _list_industries: list = dataclasses.field(repr=False, default_factory=list)

    _float_average_change_percent_all_industries: float = dataclasses.field(repr=False, default=0)

    _int_num_industries: int = dataclasses.field(repr=False, default=0)

    def __init__(self, str_working_directory: Optional[str] = None,
                 str_data_base_filename: Optional[str] = None) -> None:
        super().__init__()

        # init myTuple
        self._index_tuple = myTuple.MyTuple

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        # init working directory for Data Base
        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

        else:

            self._my_file.set_directory(myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_DIR_NAME)

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myIndustriesTimeSeriesDefinitions.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myIndustriesTimeSeriesDefinitions.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_industries_time_series = myTableSQLIndustriesTimeSeries.MyTableSQLIndustriesTimeSeries(
            self._my_sql_connection,
            self._my_sql_cursor)

        self._list_column_names = self._my_table_sql_industries_time_series.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myIndustriesTimeSeriesDefinitions.LIST_INDUSTRIES_TIME_SERIES_COLUMN_NAMES

        self._int_num_columns = self._list_column_names.__len__()

        self._init_watch_list_column_indices()

        self._init_watch_list_column_names()

        self._list_industries_tuples = myIndustriesTimeSeriesDefinitions.LIST_INIT_INDUSTRIES_TUPLES

        self._extract_industries_names_from_list_of_tuples()

    def _init_watch_list_column_indices(self) -> None:

        self._int_industries_time_series_industries_name_column_index = self._list_column_names.index(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES[
                self._index_tuple.OPTION_NAME])

        self._int_industries_time_series_quote_numbers_column_index = self._list_column_names.index(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_QUOTE_NUMBERS[
                self._index_tuple.OPTION_NAME])

        self._int_industries_time_series_change_percent_column_index = self._list_column_names.index(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_CHANGE_PERCENT[
                self._index_tuple.OPTION_NAME])

        self._int_industries_time_series_twenty_day_change_percent_json_array_column_index = self._list_column_names.index(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY[
                self._index_tuple.OPTION_NAME])

    def _init_watch_list_column_names(self) -> None:

        self._str_industries_time_series_industries_name_column_name = (
            self._list_column_names)[self._int_industries_time_series_industries_name_column_index]

        self._str_industries_time_series_quote_numbers_column_name =(
            self._list_column_names)[self._int_industries_time_series_quote_numbers_column_index]

        self._str_industries_time_series_change_percent_column_name = (
            self._list_column_names)[self._int_industries_time_series_change_percent_column_index]

        self._str_industries_time_series_twenty_day_change_percent_json_array_column_name = (
            self._list_column_names)[self._int_industries_time_series_twenty_day_change_percent_json_array_column_index]

    def _extract_industries_names_from_list_of_tuples(self) -> None:

        self._list_industries = [text for text, number in self._list_industries_tuples if text != ""]

    def get_entire_data_base_file_name(self) -> str:

        return self._my_file.get_entire_file_name

    def get_table_column_names(self) -> list:

        return self._list_column_names

    def get_table_data(self) -> list:

        return self._my_table_sql_industries_time_series.get_table_all_data()

    def get_table_data_plus_headline(self) -> list:

        headline = []

        if isinstance(self._my_table_sql_industries_time_series.get_column_names(), list):

            if all(isinstance(x, str) for x in self._my_table_sql_industries_time_series.get_column_names()):

                headline = [tuple(self._my_table_sql_industries_time_series.get_column_names())]

        self.get_sum_quotes_all_industries()

        self.get_average_change_percent_all_industries()

        data = self.get_table_data()

        data.insert(0, ('Total', self._int_num_industries, self._float_average_change_percent_all_industries, ''))

        data.insert(0, headline[0])

        return data

    def get_average_change_percent_all_industries(self) -> float:

        self._float_average_change_percent_all_industries = self._my_table_sql_industries_time_series.get_global_average_change_percent()

        return self._float_average_change_percent_all_industries

    def get_sum_quotes_all_industries(self) -> int:

        self._int_num_industries = self._my_table_sql_industries_time_series.get_global_sum_all_industries()

        return self._int_num_industries

    def set_working_directory(self, str_working_directory: str) -> None:

        try:

            if str_working_directory == '' or str_working_directory is None:

                raise ValueError(f'----- Value Error in {__title__}, {self.set_working_directory.__name__}: '
                                     f'the working directory input is empty! -----')

            elif not os.path.isdir(str_working_directory):

                raise FileExistsError(f'----- Error in {__title__}, {self.set_working_directory.__name__}: '
                                     f'the working directory {str_working_directory} does not exist! -----')

            elif not isinstance(str_working_directory, str):

                raise ValueError(f'----- Value Error in {__title__}, {self.set_working_directory.__name__}: '
                                     f'the working directory input {str_working_directory} must be a string! -----')

            else:

                self._my_file.set_directory(str_working_directory)

        except ValueError as e:

            print(e)
            exit(1)

        except FileExistsError as e:

            print(e)
            exit(1)

    def set_list_industries_tuples(self, list_industries_tuples: list[tuple[str, int]]) -> None:

        # remove tuples with empty str
        list_industries_tuples = [tup for tup in list_industries_tuples if tup[0] != ""]

        try:

            if list_industries_tuples.__len__() == 0:

                raise ValueError(f'----- Value Error in {__title__}, {self.set_list_industries_tuples.__name__}: '
                                 f'the list providing the sectors is empty! -----')

            else:

                self._list_industries_tuples = list_industries_tuples

                self._extract_industries_names_from_list_of_tuples()

        except ValueError as e:

            print(e)
            exit(1)

    def set_list_industries_percent_changes_tuples(self, list_change_percent: list[tuple]) -> None:

        self._list_change_percent_tuples = list_change_percent

    def update_industries(self) -> None:

        self._my_table_sql_industries_time_series.update_industries(self._list_industries)

        self._my_table_sql_industries_time_series.update_number_quotations(self._list_industries_tuples)

    def update_change_percent(self)  -> None:

        self._my_table_sql_industries_time_series.update_change_percent(self._list_change_percent_tuples)

if __name__ == "__main__":
    my_industries_time_series = MyIndustriesTimeSeries('/Users/oliverrudow/PycharmProjects/Data', 'time_series_data_base.db')
    # my_sector_time_series.update_sectors()
    print(my_industries_time_series.get_table_data_plus_headline())
    # print(my_sector_time_series.get_average_change_percent_all_sectors())
    # print(my_sector_time_series.get_sum_quotes_all_sectors())
    my_industries_time_series.close_sql_data_base()
