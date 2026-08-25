"""myTableSQLScoresTimeSeries.py."""

__title__: str = "myTableSQLScoresTimeSeries.py"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import mySQLDataBase, myTableSQL
from mytimeseries import myScoresTimeSeriesDefinitions
from mysharesdefinition import myRankingWatchListDefinitions


@dataclasses.dataclass(init=False)
class MyTableSQLScoresTimeSeries(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_static_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

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

    # value
    _str_scores_time_series_quote_isin_value: str = dataclasses.field(repr=False, default='')
    _b_scores_time_series_analyst_score_value: int | str = dataclasses.field(repr=False, default='')
    _b_scores_time_series_derivate_score_value: float | str = dataclasses.field(repr=False, default='')
    _b_scores_time_series_fundamental_score_value: bytes | str = dataclasses.field(repr=False, default='')
    _b_scores_time_series_performance_score_value: bytes | str = dataclasses.field(repr=False, default='')
    _b_scores_time_series_overall_score_value: bytes | str = dataclasses.field(repr=False, default='')

    # source column names
    _str_ranking_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_analyst_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_derivate_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_fundamentals_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_performance_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_overall_score_column_name: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myScoresTimeSeriesDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myScoresTimeSeriesDefinitions.STR_DATA_BASE_TABLE_NAME)

        # column quote isin
        my_special_tuple = myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column analyst score
        my_special_tuple = myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_ANALYST_SCORE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column derivate score
        my_special_tuple = myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_DERIVATE_SCORE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column fundamentals score
        my_special_tuple = myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_FUNDAMENTALS_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column performance score
        my_special_tuple = myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_PERFORMANCE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column overall score
        my_special_tuple = myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_OVERALL_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_table_columns()

        self._init_source_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

    def _init_table_columns(self) -> None:

        self._str_scores_time_series_quote_isin_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN)

        self._int_scores_time_series_quote_isin_column_index = self.get_column_index_from_list(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN)

        self._str_scores_time_series_analyst_score_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_ANALYST_SCORE)

        self._int_scores_time_series_analyst_score_column_index = self.get_column_index_from_list(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_ANALYST_SCORE)

        self._str_scores_time_series_derivate_score_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_DERIVATE_SCORE)

        self._int_scores_time_series_derivate_score_column_index = self.get_column_index_from_list(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_DERIVATE_SCORE)

        self._str_scores_time_series_fundamentals_score_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_FUNDAMENTALS_SCORE)

        self._int_scores_time_series_fundamentals_score_column_index = self.get_column_index_from_list(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_FUNDAMENTALS_SCORE)

        self._str_scores_time_series_performance_score_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_PERFORMANCE_SCORE)

        self._int_scores_time_series_performance_score_column_index = self.get_column_index_from_list(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_PERFORMANCE_SCORE)

        self._str_scores_time_series_overall_score_column_name = self.get_column_name_from_dict(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_OVERALL_SCORE)

        self._int_scores_time_series_overall_score_column_index = self.get_column_index_from_list(
            myScoresTimeSeriesDefinitions.TUPLE_SCORES_TIME_SERIES_OVERALL_SCORE)

    def _init_source_columns(self) -> None:

        self._str_ranking_watch_list_quote_isin_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_analyst_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_derivate_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_fundamentals_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_performance_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_overall_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE[self._index_tuple.DATA_CONTENT][0])

    def update_analyst_score_values(self, str_ranking_data_base_file_name: str, ranking_table_name: str):

        str_target_array_col =  self._str_scores_time_series_analyst_score_column_name
        str_target_quote_isin = self._str_scores_time_series_quote_isin_column_name
        num_array_fields = myScoresTimeSeriesDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA

        str_source_quote_isin = self._str_ranking_watch_list_quote_isin_column_name
        str_source_score_col = self._str_ranking_watch_list_analyst_score_column_name

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{str_ranking_data_base_file_name}" AS db_ranking')

                # 3. SQL-Query mit Platzhaltern (?) statt String-Formatierung
                # Das UPDATE wurde so umgeschrieben, dass es ALLE ISINs auf einmal verarbeitet
                # SQL-Query: Begrenzt die Array-Elemente pro ISIN auf maximal 20
                sql_update = f"""
                    INSERT INTO {self._str_sql_schema}.{self._str_table_name} (
                        {str_target_quote_isin}, 
                        {str_target_array_col}
                    )
                    SELECT 
                        src.{str_source_quote_isin}, 
                        json_array(src.{str_source_score_col})
                    FROM db_ranking.{ranking_table_name} AS src
                    WHERE src.{str_source_score_col} IS NOT NULL 
                    ON CONFLICT({str_target_quote_isin}) DO UPDATE SET 
                        {str_target_array_col} = (
                            SELECT json_group_array(value)
                            FROM (
                                -- HIER WAR DER FEHLER: Wir nutzen excluded statt src
                                SELECT json_extract(excluded.{str_target_array_col}, '$[0]') AS value

                                UNION ALL

                                SELECT value
                                FROM json_each(ifnull({self._str_sql_schema}.{self._str_table_name}.{str_target_array_col}, '[]'))
                                LIMIT {num_array_fields}
                            ) 
                        )
                """

                self._my_sql_cursor.execute(sql_update)

                # 5. Nur EIN Commit nach allen Updates (enormer Geschwindigkeitsvorteil)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, {self.update_analyst_score_values.__name__} ----\n'
                    f'---- An error occurred during database operations: {err} ----'
                )

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_ranking')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

    def update_derivate_score_values(self, str_ranking_data_base_file_name: str, ranking_table_name: str):

        str_target_array_col =  self._str_scores_time_series_derivate_score_column_name
        str_target_quote_isin = self._str_scores_time_series_quote_isin_column_name
        num_array_fields = myScoresTimeSeriesDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA

        str_source_quote_isin = self._str_ranking_watch_list_quote_isin_column_name
        str_source_score_col = self._str_ranking_watch_list_derivate_score_column_name

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{str_ranking_data_base_file_name}" AS db_ranking')

                # 3. SQL-Query mit Platzhaltern (?) statt String-Formatierung
                # Das UPDATE wurde so umgeschrieben, dass es ALLE ISINs auf einmal verarbeitet
                # SQL-Query: Begrenzt die Array-Elemente pro ISIN auf maximal 20
                sql_update = f"""
                    INSERT INTO {self._str_sql_schema}.{self._str_table_name} (
                        {str_target_quote_isin}, 
                        {str_target_array_col}
                    )
                    SELECT 
                        src.{str_source_quote_isin}, 
                        json_array(src.{str_source_score_col})
                    FROM db_ranking.{ranking_table_name} AS src
                    WHERE src.{str_source_score_col} IS NOT NULL 
                    ON CONFLICT({str_target_quote_isin}) DO UPDATE SET 
                        {str_target_array_col} = (
                            SELECT json_group_array(value)
                            FROM (
                                -- HIER WAR DER FEHLER: Wir nutzen excluded statt src
                                SELECT json_extract(excluded.{str_target_array_col}, '$[0]') AS value

                                UNION ALL

                                SELECT value
                                FROM json_each(ifnull({self._str_sql_schema}.{self._str_table_name}.{str_target_array_col}, '[]'))
                                LIMIT {num_array_fields}
                            ) 
                        )
                """

                self._my_sql_cursor.execute(sql_update)

                # 5. Nur EIN Commit nach allen Updates (enormer Geschwindigkeitsvorteil)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, {self.update_derivate_score_values.__name__} ----\n'
                    f'---- An error occurred during database operations: {err} ----'
                )

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_ranking')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

    def update_fundamental_score_values(self, str_ranking_data_base_file_name: str, ranking_table_name: str):

        str_target_array_col = self._str_scores_time_series_fundamentals_score_column_name
        str_target_quote_isin = self._str_scores_time_series_quote_isin_column_name
        num_array_fields = myScoresTimeSeriesDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA

        str_source_quote_isin = self._str_ranking_watch_list_quote_isin_column_name
        str_source_score_col = self._str_ranking_watch_list_fundamentals_score_column_name

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{str_ranking_data_base_file_name}" AS db_ranking')

                # 3. SQL-Query mit Platzhaltern (?) statt String-Formatierung
                # Das UPDATE wurde so umgeschrieben, dass es ALLE ISINs auf einmal verarbeitet
                # SQL-Query: Begrenzt die Array-Elemente pro ISIN auf maximal 20
                sql_update = f"""
                       INSERT INTO {self._str_sql_schema}.{self._str_table_name} (
                           {str_target_quote_isin}, 
                           {str_target_array_col}
                       )
                       SELECT 
                           src.{str_source_quote_isin}, 
                           json_array(src.{str_source_score_col})
                       FROM db_ranking.{ranking_table_name} AS src
                       WHERE src.{str_source_score_col} IS NOT NULL 
                       ON CONFLICT({str_target_quote_isin}) DO UPDATE SET 
                           {str_target_array_col} = (
                               SELECT json_group_array(value)
                               FROM (
                                   -- HIER WAR DER FEHLER: Wir nutzen excluded statt src
                                   SELECT json_extract(excluded.{str_target_array_col}, '$[0]') AS value

                                   UNION ALL

                                   SELECT value
                                   FROM json_each(ifnull({self._str_sql_schema}.{self._str_table_name}.{str_target_array_col}, '[]'))
                                   LIMIT {num_array_fields}
                               ) 
                           )
                   """

                self._my_sql_cursor.execute(sql_update)

                # 5. Nur EIN Commit nach allen Updates (enormer Geschwindigkeitsvorteil)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, {self.update_fundamental_score_values.__name__} ----\n'
                    f'---- An error occurred during database operations: {err} ----'
                )

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_ranking')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

    def update_performance_score_values(self, str_ranking_data_base_file_name: str, ranking_table_name: str):

        str_target_array_col = self._str_scores_time_series_performance_score_column_name
        str_target_quote_isin = self._str_scores_time_series_quote_isin_column_name
        num_array_fields = myScoresTimeSeriesDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA

        str_source_quote_isin = self._str_ranking_watch_list_quote_isin_column_name
        str_source_score_col = self._str_ranking_watch_list_performance_score_column_name

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{str_ranking_data_base_file_name}" AS db_ranking')

                # 3. SQL-Query mit Platzhaltern (?) statt String-Formatierung
                # Das UPDATE wurde so umgeschrieben, dass es ALLE ISINs auf einmal verarbeitet
                # SQL-Query: Begrenzt die Array-Elemente pro ISIN auf maximal 20
                sql_update = f"""
                       INSERT INTO {self._str_sql_schema}.{self._str_table_name} (
                           {str_target_quote_isin}, 
                           {str_target_array_col}
                       )
                       SELECT 
                           src.{str_source_quote_isin}, 
                           json_array(src.{str_source_score_col})
                       FROM db_ranking.{ranking_table_name} AS src
                       WHERE src.{str_source_score_col} IS NOT NULL 
                       ON CONFLICT({str_target_quote_isin}) DO UPDATE SET 
                           {str_target_array_col} = (
                               SELECT json_group_array(value)
                               FROM (
                                   -- HIER WAR DER FEHLER: Wir nutzen excluded statt src
                                   SELECT json_extract(excluded.{str_target_array_col}, '$[0]') AS value

                                   UNION ALL

                                   SELECT value
                                   FROM json_each(ifnull({self._str_sql_schema}.{self._str_table_name}.{str_target_array_col}, '[]'))
                                   LIMIT {num_array_fields}
                               ) 
                           )
                   """

                self._my_sql_cursor.execute(sql_update)

                # 5. Nur EIN Commit nach allen Updates (enormer Geschwindigkeitsvorteil)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, {self.update_performance_score_values.__name__} ----\n'
                    f'---- An error occurred during database operations: {err} ----'
                )

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_ranking')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

    def update_overall_score_values(self, str_ranking_data_base_file_name: str, ranking_table_name: str):

        str_target_array_col = self._str_scores_time_series_overall_score_column_name
        str_target_quote_isin = self._str_scores_time_series_quote_isin_column_name
        num_array_fields = myScoresTimeSeriesDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA

        str_source_quote_isin = self._str_ranking_watch_list_quote_isin_column_name
        str_source_score_col = self._str_ranking_watch_list_overall_score_column_name

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{str_ranking_data_base_file_name}" AS db_ranking')

                # 3. SQL-Query mit Platzhaltern (?) statt String-Formatierung
                # Das UPDATE wurde so umgeschrieben, dass es ALLE ISINs auf einmal verarbeitet
                # SQL-Query: Begrenzt die Array-Elemente pro ISIN auf maximal 20
                sql_update = f"""
                          INSERT INTO {self._str_sql_schema}.{self._str_table_name} (
                              {str_target_quote_isin}, 
                              {str_target_array_col}
                          )
                          SELECT 
                              src.{str_source_quote_isin}, 
                              json_array(src.{str_source_score_col})
                          FROM db_ranking.{ranking_table_name} AS src
                          WHERE src.{str_source_score_col} IS NOT NULL 
                          ON CONFLICT({str_target_quote_isin}) DO UPDATE SET 
                              {str_target_array_col} = (
                                  SELECT json_group_array(value)
                                  FROM (
                                      -- HIER WAR DER FEHLER: Wir nutzen excluded statt src
                                      SELECT json_extract(excluded.{str_target_array_col}, '$[0]') AS value

                                      UNION ALL

                                      SELECT value
                                      FROM json_each(ifnull({self._str_sql_schema}.{self._str_table_name}.{str_target_array_col}, '[]'))
                                      LIMIT {num_array_fields}
                                  ) 
                              )
                      """

                self._my_sql_cursor.execute(sql_update)

                # 5. Nur EIN Commit nach allen Updates (enormer Geschwindigkeitsvorteil)
                self._my_sql_connection.commit()

            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, {self.update_overall_score_values.__name__} ----\n'
                    f'---- An error occurred during database operations: {err} ----'
                )

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_ranking')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
