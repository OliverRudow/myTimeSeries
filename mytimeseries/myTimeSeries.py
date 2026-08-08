"""myTimeSeries.py."""

__title__: str = "myTimeSeries"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
from typing import Optional
from mydatabase import mySQLDataBase
from myfilebase import myFileBase
from mytimeseries import myIndustriesTimeSeriesDefinitions, myIndustriesTimeSeries, myTableSQLUpdateManager
from mytimeseries import mySectorsTimeSeries


@dataclasses.dataclass(init=False)
class MyTimeSeries(mySQLDataBase.MySQLDataBase):
    """

    """
    # Data Base Working Directory
    _str_working_directory: str = dataclasses.field(init=False, default_factory=str)

    # Data Base File Name
    _str_data_base_file_name: str = dataclasses.field(init=False, default_factory=str)

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # Industries Time Series
    _my_industries_time_series: myIndustriesTimeSeries.MyIndustriesTimeSeries = (
        dataclasses.field(repr=False, default_factory=type(myIndustriesTimeSeries.MyIndustriesTimeSeries)))

    # Sector Time Series
    _my_sectors_time_series: mySectorsTimeSeries.MySectorsTimeSeries = (
        dataclasses.field(repr=False, default_factory=type(mySectorsTimeSeries.MySectorsTimeSeries)))

    # Update Manager
    _my_table_sql_update_manager: myTableSQLUpdateManager.MyTableSQLUpdateManager = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLUpdateManager.MyTableSQLUpdateManager)))

    _bool_update_permission: bool = dataclasses.field(init=False, default=False)


    def __init__(self, str_working_directory: Optional[str] = None,
                 str_data_base_filename: Optional[str] = None) -> None:
        super().__init__()

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        # init working directory for Data Base
        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

            self._str_working_directory = str_working_directory

        else:

            self._my_file.set_directory(myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_DIR_NAME)

            self._str_working_directory = myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_DIR_NAME

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

            self._str_data_base_file_name = str_data_base_filename

        else:

            self._my_file.set_file_name(myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_FILE_NAME)

            self._str_data_base_file_name = myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_FILE_NAME

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myIndustriesTimeSeriesDefinitions.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myIndustriesTimeSeriesDefinitions.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_industries_time_series = myIndustriesTimeSeries.MyIndustriesTimeSeries(self._str_working_directory,
                                                                                        self._str_data_base_file_name)

        self._my_sectors_time_series = mySectorsTimeSeries.MySectorsTimeSeries(self._str_working_directory,
                                                                               self._str_data_base_file_name)

        self._my_table_sql_update_manager = myTableSQLUpdateManager.MyTableSQLUpdateManager(self._my_sql_connection,
                                                                                self._my_sql_cursor)

        self._bool_update_permission = self._my_table_sql_update_manager.check_update_time_series_permission()

    def update_sectors(self, list_sectors: list) -> None:

        if self._bool_update_permission:

            self._my_sectors_time_series.set_list_sector_tuples(list_sectors)

            self._my_sectors_time_series.update_sectors()

    def update_sectors_change_percent(self, list_change_percent: list[tuple]):

        if self._bool_update_permission:

            self._my_sectors_time_series.set_list_sector_percent_changes_tuples(list_change_percent)

            self._my_sectors_time_series.update_change_percent()

    def update_industries(self, list_industries: list) -> None:

        if self._bool_update_permission:

            self._my_industries_time_series.set_list_industries_tuples(list_industries)

            self._my_industries_time_series.update_industries()

    def update_industries_change_percent(self, list_industries_change_percent: list[tuple]):

        if self._bool_update_permission:

            self._my_industries_time_series.set_list_industries_percent_changes_tuples(list_industries_change_percent)

            self._my_industries_time_series.update_change_percent()

    def _update_date(self):

        self._my_table_sql_update_manager.set_update_date()

    def exit_time_series(self):

        self._update_date()

        self._my_industries_time_series.close_sql_data_base()

        self._my_sectors_time_series.close_sql_data_base()

if __name__ == "__main__":
    my_time_series = MyTimeSeries('/Users/oliverrudow/PycharmProjects/Data', 'time_series_data_base.db')
