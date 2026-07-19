"""mySectorsTimeSeries.py."""

__title__: str = "mySectorsTimeSeries"
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
from mytimeseries import mySectorsTimeSeriesDefinitions
from mytimeseries import myTableSQLSectorsTimeSeries


@dataclasses.dataclass(init=False)
class MySectorsTimeSeries(mySQLDataBase.MySQLDataBase):
    """

    """
    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # SQL Table Static Watch List
    _my_table_sql_sectors_time_series: myTableSQLSectorsTimeSeries.MyTableSQLSectorsTimeSeries = (
        dataclasses.field(repr=False, default=None))

    # tuple indices
    _int_sectors_time_series_sector_name_column_index: int = dataclasses.field(repr=False, default=0)
    _int_sectors_time_series_quote_numbers_column_index: int = dataclasses.field(repr=False, default=0)
    _int_sectors_time_series_change_percent_column_index: int = dataclasses.field(repr=False, default=0)
    _int_sectors_time_series_twenty_day_change_percent_json_array_column_index: int = dataclasses.field(repr=False, default=0)

    _str_sectors_time_series_sector_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_sectors_time_series_quote_numbers_column_name: str = dataclasses.field(repr=False, default='')
    _str_sectors_time_series_change_percent_column_name: str = dataclasses.field(repr=False, default='')
    _str_sectors_time_series_twenty_day_change_percent_json_array_column_name: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default=list)

    _int_num_columns: int = dataclasses.field(repr=False, default=0)

    _list_sectors_tuples: list[tuple[str, int]] = dataclasses.field(repr=False, default=list)

    _list_change_percent_tuples: list[tuple] = dataclasses.field(repr=False, default=list)

    _list_sectors: list = dataclasses.field(repr=False, default=list)

    _float_average_change_percent_all_sectors: float = dataclasses.field(repr=False, default=0)

    _int_num_sectors: int = dataclasses.field(repr=False, default=0)

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

            self._my_file.set_directory(mySectorsTimeSeriesDefinitions.STR_DATA_BASE_DIR_NAME)

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(mySectorsTimeSeriesDefinitions.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(mySectorsTimeSeriesDefinitions.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(mySectorsTimeSeriesDefinitions.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_sectors_time_series = myTableSQLSectorsTimeSeries.MyTableSQLSectorsTimeSeries(
            self._my_sql_connection,
            self._my_sql_cursor)

        self._list_column_names = self._my_table_sql_sectors_time_series.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = mySectorsTimeSeriesDefinitions.LIST_SECTORS_TIME_SERIES_COLUMN_NAMES

        self._int_num_columns = self._list_column_names.__len__()

        self._init_watch_list_column_indices()

        self._init_watch_list_column_names()

        self._list_sectors_tuples = mySectorsTimeSeriesDefinitions.LIST_INIT_SECTOR_TUPLES

        self._extract_sector_names_from_list_of_tuples()

    def _init_watch_list_column_indices(self) -> None:

        self._int_sectors_time_series_sector_name_column_index = self._list_column_names.index(
            mySectorsTimeSeriesDefinitions.TUPLE_SECTORS_TIME_SERIES_SECTORS[
                self._index_tuple.OPTION_NAME])

        self._int_sectors_time_series_quote_numbers_column_index = self._list_column_names.index(
            mySectorsTimeSeriesDefinitions.TUPLE_SECTORS_TIME_SERIES_QUOTE_NUMBERS[
                self._index_tuple.OPTION_NAME])

        self._int_sectors_time_series_change_percent_column_index = self._list_column_names.index(
            mySectorsTimeSeriesDefinitions.TUPLE_SECTORS_TIME_SERIES_CHANGE_PERCENT[
                self._index_tuple.OPTION_NAME])

        self._int_sectors_time_series_twenty_day_change_percent_json_array_column_index = self._list_column_names.index(
            mySectorsTimeSeriesDefinitions.TUPLE_SECTORS_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY[
                self._index_tuple.OPTION_NAME])

    def _init_watch_list_column_names(self) -> None:

        self._str_sectors_time_series_sector_name_column_name = (
            self._list_column_names)[self._int_sectors_time_series_sector_name_column_index]

        self._str_sectors_time_series_quote_numbers_column_name =(
            self._list_column_names)[self._int_sectors_time_series_quote_numbers_column_index]

        self._str_sectors_time_series_change_percent_column_name = (
            self._list_column_names)[self._int_sectors_time_series_change_percent_column_index]

        self._str_sectors_time_series_twenty_day_change_percent_json_array_column_name = (
            self._list_column_names)[self._int_sectors_time_series_twenty_day_change_percent_json_array_column_index]

    def _extract_sector_names_from_list_of_tuples(self) -> None:

        self._list_sectors = [text for text, number in self._list_sectors_tuples if text != ""]

    def get_entire_data_base_file_name(self) -> str:

        return self._my_file.get_entire_file_name

    def get_table_column_names(self) -> list:

        return self._list_column_names

    def get_table_data(self) -> list:

        return self._my_table_sql_sectors_time_series.get_table_all_data()

    def get_table_data_plus_headline(self) -> list:

        headline = []

        data = []

        if isinstance(self._my_table_sql_sectors_time_series.get_column_names(), list):

            if all(isinstance(x, str) for x in self._my_table_sql_sectors_time_series.get_column_names()):

                headline = [tuple(self._my_table_sql_sectors_time_series.get_column_names())]

        self.get_sum_quotes_all_sectors()

        self.get_average_change_percent_all_sectors()

        data = self.get_table_data()

        data.insert(0, ('Total', self._int_num_sectors, self._float_average_change_percent_all_sectors, ''))

        data.insert(0, headline[0])

        return data

    def get_average_change_percent_all_sectors(self) -> float:

        self._float_average_change_percent_all_sectors = self._my_table_sql_sectors_time_series.get_global_average_change_percent()

        return self._float_average_change_percent_all_sectors

    def get_sum_quotes_all_sectors(self) -> int:

        self._int_num_sectors = self._my_table_sql_sectors_time_series.get_global_sum_all_sectors()

        return self._int_num_sectors

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

    def set_list_sector_tuples(self, list_sector_tuples: list[tuple[str, int]]) -> None:

        # remove tuples with empty str
        list_sector_tuples = [tup for tup in list_sector_tuples if tup[0] != ""]

        try:

            if list_sector_tuples.__len__() == 0:

                raise ValueError(f'----- Value Error in {__title__}, {self.set_list_sector_tuples.__name__}: '
                                 f'the list providing the sectors is empty! -----')

            else:

                self._list_sectors_tuples = list_sector_tuples

                self._extract_sector_names_from_list_of_tuples()

        except ValueError as e:

            print(e)
            exit(1)

    def set_list_sector_percent_changes_tuples(self, list_change_percent: list[tuple]) -> None:

        self._list_change_percent_tuples = list_change_percent

    def update_sectors(self) -> None:

        self._my_table_sql_sectors_time_series.update_sectors(self._list_sectors)

        self._my_table_sql_sectors_time_series.update_number_quotations(self._list_sectors_tuples)

    def update_change_percent(self)  -> None:

        self._my_table_sql_sectors_time_series.update_change_percent(self._list_change_percent_tuples)

if __name__ == "__main__":
    my_sector_time_series = MySectorsTimeSeries('/Users/oliverrudow/PycharmProjects/Data', 'time_series_data_base.db')
    # my_sector_time_series.update_sectors()
    print(my_sector_time_series.get_table_data_plus_headline())
    # print(my_sector_time_series.get_average_change_percent_all_sectors())
    # print(my_sector_time_series.get_sum_quotes_all_sectors())
    my_sector_time_series.close_sql_data_base()
