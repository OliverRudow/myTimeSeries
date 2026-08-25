"""myScoresTimeSeries.py."""

__title__: str = "myScoresTimeSeries"
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
from mytimeseries import myScoresTimeSeriesDefinitions
from mytimeseries import myTableSQLScoresTimeSeries
from mysharesdefinition import myRankingWatchListDefinitions

STR_RANKING_DATA_BASE_NAME: str = '/Users/oliverrudow/PycharmProjects/Data/shares_data_base.db'

@dataclasses.dataclass(init=False)
class MyScoresTimeSeries(mySQLDataBase.MySQLDataBase):
    """

    """
    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # SQL Table Static Watch List
    _my_table_sql_scores_time_series: myTableSQLScoresTimeSeries.MyTableSQLScoresTimeSeries = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLScoresTimeSeries.MyTableSQLScoresTimeSeries)))

    # column indices
    _int_scores_time_series_quote_isin_column_index: int = dataclasses.field(repr=False, default=0)
    _int_scores_time_series_analyst_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_scores_time_series_derivate_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_scores_time_series_fundamentals_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_scores_time_series_performance_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_scores_time_series_overall_score_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_scores_time_series_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_scores_time_series_analyst_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_scores_time_series_derivate_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_scores_time_series_fundamentals_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_scores_time_series_performance_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_scores_time_series_overall_score_column_name: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    _int_num_columns: int = dataclasses.field(repr=False, default=0)

    # ranking watch list
    _str_ranking_data_base_file_name: str = dataclasses.field(repr=False, default='')

    _ranking_table_name: str = dataclasses.field(repr=False, default='')

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

            self._my_file.set_directory(myScoresTimeSeriesDefinitions.STR_DATA_BASE_DIR_NAME)

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(myScoresTimeSeriesDefinitions.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myScoresTimeSeriesDefinitions.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myScoresTimeSeriesDefinitions.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_sectors_time_series = myTableSQLScoresTimeSeries.MyTableSQLScoresTimeSeries(
            self._my_sql_connection,
            self._my_sql_cursor)

        self._list_column_names =  self._my_table_sql_sectors_time_series.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myScoresTimeSeriesDefinitions.LIST_SCORES_TIME_SERIES_COLUMN_NAMES

        self._int_num_columns = self._list_column_names.__len__()

        self._init_watch_list_column_indices()

        self._init_watch_list_column_names()

        self._str_ranking_data_base_file_name = STR_RANKING_DATA_BASE_NAME

        self._ranking_table_name = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME


    def _init_watch_list_column_indices(self) -> None:

        self._int_scores_time_series_quote_isin_column_index = self._list_column_names.index(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN[
                self._index_tuple.OPTION_NAME])

        self._int_scores_time_series_analyst_score_column_index = self._list_column_names.index(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_ANALYST_SCORE[
                self._index_tuple.OPTION_NAME])

        self._int_scores_time_series_derivate_score_column_index = self._list_column_names.index(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_DERIVATE_SCORE[
                self._index_tuple.OPTION_NAME])

        self._int_scores_time_series_fundamentals_score_column_index = self._list_column_names.index(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_FUNDAMENTALS_SCORE[
                self._index_tuple.OPTION_NAME])

        self._int_scores_time_series_performance_score_column_index = self._list_column_names.index(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_PERFORMANCE_SCORE[
                self._index_tuple.OPTION_NAME])

        self._int_scores_time_series_overall_score_column_index = self._list_column_names.index(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_OVERALL_SCORE[
                self._index_tuple.OPTION_NAME])

    def _init_watch_list_column_names(self) -> None:

        self._str_scores_time_series_quote_isin_column_name = (
            self._list_column_names)[self._int_scores_time_series_quote_isin_column_index]

        self._str_scores_time_series_analyst_score_column_name =(
            self._list_column_names)[self._int_scores_time_series_analyst_score_column_index]

        self._str_scores_time_series_derivate_score_column_name = (
            self._list_column_names)[self._int_scores_time_series_derivate_score_column_index]

        self._str_scores_time_series_fundamentals_score_column_name = (
            self._list_column_names)[self._int_scores_time_series_fundamentals_score_column_index]

        self._str_scores_time_series_performance_score_column_name = (
            self._list_column_names)[ self._int_scores_time_series_performance_score_column_index]

        self._str_scores_time_series_overall_score_column_name = (
            self._list_column_names)[self._int_scores_time_series_overall_score_column_index]

    def get_entire_data_base_file_name(self) -> str:

        return self._my_file.get_entire_file_name

    def get_table_column_names(self) -> list:

        return self._list_column_names

    def update_all_score_values(self) -> None:

        self._my_table_sql_sectors_time_series.update_analyst_score_values(self._str_ranking_data_base_file_name,
                                                                           self._ranking_table_name)

        self._my_table_sql_sectors_time_series.update_derivate_score_values(self._str_ranking_data_base_file_name,
                                                                           self._ranking_table_name)

        self._my_table_sql_sectors_time_series.update_fundamental_score_values(self._str_ranking_data_base_file_name,
                                                                            self._ranking_table_name)

        self._my_table_sql_sectors_time_series.update_performance_score_values(self._str_ranking_data_base_file_name,
                                                                               self._ranking_table_name)

        self._my_table_sql_sectors_time_series.update_overall_score_values(self._str_ranking_data_base_file_name,
                                                                               self._ranking_table_name)

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


if __name__ == "__main__":
    my_scores_time_series = MyScoresTimeSeries('/Users/oliverrudow/PycharmProjects/Data', 'time_series_data_base.db')
    my_scores_time_series.update_all_score_values()
    # my_sector_time_series.update_sectors()
    # print(my_sector_time_series.get_average_change_percent_all_sectors())
    # print(my_sector_time_series.get_sum_quotes_all_sectors())
    my_scores_time_series.close_sql_data_base()
