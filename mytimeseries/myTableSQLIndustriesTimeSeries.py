"""myTableSQLIndustriesTimeSeries.py."""

__title__: str = "myTableSQLIndustriesTimeSeries.py"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import mySQLDataBase, myTableSQL
from mytimeseries import myIndustriesTimeSeriesDefinitions


@dataclasses.dataclass(init=False)
class MyTableSQLIndustriesTimeSeries(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_static_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_industries_time_series_industries_name_column_index: int = dataclasses.field(repr=False, default=0)
    _int_industries_time_series_quote_numbers_column_index: int = dataclasses.field(repr=False, default=0)
    _int_industries_time_series_change_percent_column_index: int = dataclasses.field(repr=False, default=0)
    _int_industries_time_series_twenty_day_change_percent_json_array_column_index: int = dataclasses.field(repr=False,
                                                                                                         default=0)
    # column names
    _str_industries_time_series_industries_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_industries_time_series_quote_numbers_column_name: str = dataclasses.field(repr=False, default='')
    _str_industries_time_series_change_percent_column_name: str = dataclasses.field(repr=False, default='')
    _str_industries_time_series_twenty_day_change_percent_json_array_column_name: str = dataclasses.field(repr=False,
                                                                                                        default='')
    # value
    _str_industries_time_series_industries_name_value: str = dataclasses.field(repr=False, default='')
    _int_industries_time_series_quote_numbers_value: int | str = dataclasses.field(repr=False, default='')
    _float_industries_time_series_change_percent_value: float | str = dataclasses.field(repr=False, default='')
    _b_industries_time_series_twenty_day_change_percent_json_array_credit_value: bytes | str = dataclasses.field(
        repr=False,
        default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myIndustriesTimeSeriesDefinitions.STR_DATA_BASE_TABLE_NAME)

        # column sectors name
        my_special_tuple = myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column quote numbers
        my_special_tuple =myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_QUOTE_NUMBERS

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column quote numbers
        my_special_tuple = myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_CHANGE_PERCENT

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column json array
        my_special_tuple = myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_table_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

    def _init_table_columns(self) -> None:

        self._str_industries_time_series_industries_name_column_name = self.get_column_name_from_dict(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES)

        self._int_industries_time_series_industries_name_column_index = self.get_column_index_from_list(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES)

        self._str_industries_time_series_quote_numbers_column_name = self.get_column_name_from_dict(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_QUOTE_NUMBERS)

        self._int_industries_time_series_quote_numbers_column_index = self.get_column_index_from_list(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_QUOTE_NUMBERS)

        self._str_industries_time_series_change_percent_column_name = self.get_column_name_from_dict(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_CHANGE_PERCENT)

        self._int_industries_time_series_change_percent_column_index = self.get_column_index_from_list(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_CHANGE_PERCENT)

        self._str_industries_time_series_twenty_day_change_percent_json_array_column_name = self.get_column_name_from_dict(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY)

        self._int_industries_time_series_twenty_day_change_percent_json_array_column_index = self.get_column_index_from_list(
            myIndustriesTimeSeriesDefinitions.TUPLE_INDUSTRIES_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY)

    def update_industries(self, list_industries: list[str]):

        str_text = (f' INSERT OR IGNORE INTO {self._str_sql_schema}.{self._str_table_name} '
                    f'({self._str_industries_time_series_industries_name_column_name}) VALUES (?) ')

        data = [(industry,) for industry in list_industries]

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.executemany(str_text, data)

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.update_industries.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    def update_number_quotations(self, list_tuples: list[tuple[str, int]]):

        str_text = (f'UPDATE {self._str_sql_schema}.{self._str_table_name} '
                    f'SET {self._str_industries_time_series_quote_numbers_column_name} = ? '
                    f'WHERE {self._str_industries_time_series_industries_name_column_name} = ? ')

        data = [(num_quote, industry_name) for industry_name, num_quote in list_tuples]


        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.executemany(str_text, data)

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.update_number_quotations.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    def update_change_percent(self, list_change_percents: list[tuple]):

        str_target_change_col = self._str_industries_time_series_change_percent_column_name
        str_target_array_col = self._str_industries_time_series_twenty_day_change_percent_json_array_column_name
        str_target_id = self._str_industries_time_series_industries_name_column_name
        num_array_fields = myIndustriesTimeSeriesDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA

        # SQLite code is organized as follows:
        # 1. json_insert(..., '$[0]', new_value) insert value left (Index 0).
        # 2. json_remove(..., '$[20]') removes 21. element.
        # 3. COALESCE takes care if array is empty.

        str_text = (f"UPDATE {self._str_sql_schema}.{self._str_table_name} "
                    f"SET "
                    f"{str_target_change_col} = ?, "
                    f"{str_target_array_col} = ( "
                    f" SELECT json_group_array(value) "
                    f" FROM ("
                    f"      SELECT ? AS value "
                    f""
                    f"      UNION ALL "
                    f""
                    f"      SELECT value"
                    f"      FROM json_each(IFNull({self._str_sql_schema}.{self._str_table_name}.{str_target_array_col}, '[]')) "
                    f"      LIMIT {num_array_fields}"
                    f" ) "
                    f") "
                    f"WHERE {str_target_id} = ? ")

        data = [(value, value, name) for name, number, value in list_change_percents]

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.executemany(str_text, data)

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.update_change_percent.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

    def get_global_average_change_percent(self) -> float:

        _str_change_percent_col = self._str_industries_time_series_change_percent_column_name

        _str_text = (f'SELECT '
                     f' ROUND(AVG({_str_change_percent_col}), 2) '
                     f' FROM {self._str_sql_schema}.{self._str_table_name} '
                     f' WHERE {_str_change_percent_col} <> 0 ')

        _list_result = 0

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(_str_text)

                _list_result = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(f'---- Operational Error in {__title__}, {self.get_global_average_change_percent.__name__} ----, \n'
                    f'---- the Text {_str_text} has caused an Error {err} ! ----')

                exit(1)

            if _list_result.__len__() > 0:

                _list_result =  _list_result[0][0]

            else:

                _list_result = 0

        return _list_result

    def get_global_sum_all_industries(self) -> int:

        _str_num_quotes_col = self._str_industries_time_series_quote_numbers_column_name

        _str_text = (f'SELECT '
                     f' SUM({_str_num_quotes_col}) '
                     f' FROM {self._str_sql_schema}.{self._str_table_name} ')

        _list_result = 0

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(_str_text)

                _list_result = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, {self.get_global_sum_all_industries.__name__} ----, \n'
                    f'---- the Text {_str_text} has caused an Error {err} ! ----')

                exit(1)

            if _list_result.__len__() > 0:

                _list_result = _list_result[0][0]

            else:

                _list_result = 0

        return _list_result


if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
