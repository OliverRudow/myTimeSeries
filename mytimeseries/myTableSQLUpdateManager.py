"""myTableSQLUpdateManager.py."""

__title__: str = "myTableSQLUpdateManager.py"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from datetime import date
from mydatabase import mySQLDataBase, myTableSQL
from mytimeseries import myUpdateManagerDefinitions


@dataclasses.dataclass(init=False)
class MyTableSQLUpdateManager(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_update_manager_date_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_update_manager_date_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_update_manager_date_value: str = dataclasses.field(repr=False, default='')

    # date from today
    _str_today_iso_format: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myUpdateManagerDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myUpdateManagerDefinitions.STR_DATA_BASE_TABLE_NAME)

        # today
        self._str_today_iso_format = date.today().isoformat()

        # column sectors name
        my_special_tuple = myUpdateManagerDefinitions.TUPLE_UPDATE_MANAGER_DATE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myUpdateManagerDefinitions.TUPLE_UPDATE_MANAGER_DATE)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_update_manager_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()
            self.set_update_date()

    def _init_update_manager_columns(self) -> None:

        self._str_update_manager_date_column_name = self.get_column_name_from_dict(
            myUpdateManagerDefinitions.TUPLE_UPDATE_MANAGER_DATE)

        self._int_update_manager_date_column_index = self.get_column_index_from_list(
            myUpdateManagerDefinitions.TUPLE_UPDATE_MANAGER_DATE)

    def get_update_date(self) -> float:

        _str_date = self._str_update_manager_date_column_name

        _str_text = (f'SELECT {self._str_update_manager_date_column_name} '
                     f' FROM {self._str_sql_schema}.{self._str_table_name} ')

        _list_result = 0

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(_str_text)

                _list_result = self._my_sql_cursor.fetchone()

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(f'---- Operational Error in {__title__}, {self.get_update_date.__name__} ----, \n'
                    f'---- the Text {_str_text} has caused an Error {err} ! ----')

                exit(1)

            if _list_result.__len__() > 0:

                _list_result =  _list_result[0][0]

            else:

                _list_result = 0

        return _list_result

    def set_update_date(self):

        _str_text = (f'UPDATE {self._str_sql_schema}.{self._str_table_name} '
                     f' SET {self._str_update_manager_date_column_name} = ? '
                     f' WHERE id = ?')

        _data = (self._str_today_iso_format, 1)

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(_str_text, _data)

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(f'---- Operational Error in {__title__}, {self.set_update_date.__name__} ----, \n'
                      f'---- the Text {_str_text} has caused an Error {err} ! ----')

                exit(1)

if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
