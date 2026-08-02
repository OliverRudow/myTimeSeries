"""myIndustriesTimeSeriesDefinitions.py."""

__title__: str = "myIndustriesTimeSeriesDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'industries_time_series'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 20

LIST_INIT_INDUSTRIES_TUPLES: list[tuple[str, int]] = [('Semiconductors ', 0), ('Computer Hardware', 0), ('Engineering & Construction ', 0)]

LIST_SECTIONS_WATCH_LIST: list[str] = ['INDUSTRIES_TIME_SERIES.INDUSTRIES',
                                       'INDUSTRIES_TIME_SERIES.NUMBER_QUOTES',
                                       'INDUSTRIES_TIME_SERIES.CHANGE_PERCENT',
                                       'INDUSTRIES_TIME_SERIES.TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY']

TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('INDUSTRIES_TIME_SERIES.INDUSTRIES',
    'industries',
    ('industries', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_INDUSTRIES_TIME_SERIES_QUOTE_NUMBERS: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('INDUSTRIES_TIME_SERIES.QUOTE_NUMBERS',
     'quote_numbers',
    ('quote_numbers', 'INTEGER'),
    tuple)

TUPLE_INDUSTRIES_TIME_SERIES_CHANGE_PERCENT: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('INDUSTRIES_TIME_SERIES.CHANGE_PERCENT',
     'change_percent',
    ('change_percent', 'REAL'),
    tuple)

TUPLE_INDUSTRIES_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('INDUSTRIES_TIME_SERIES.TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY',
    'twenty_day_change_percent_json_array',
    ('twenty_day_change_percent_json_array', 'BLOB'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_INDUSTRIES_TIME_SERIES_COLUMN_NAMES: list[str] = [TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES[
                                                        _index_tuple.OPTION_NAME],
                                                       TUPLE_INDUSTRIES_TIME_SERIES_QUOTE_NUMBERS[
                                                        _index_tuple.OPTION_NAME],
                                                       TUPLE_INDUSTRIES_TIME_SERIES_CHANGE_PERCENT[
                                                        _index_tuple.OPTION_NAME],
                                                       TUPLE_INDUSTRIES_TIME_SERIES_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY[
                                                        _index_tuple.OPTION_NAME]]

INDEX_PRIMARY_KEY = LIST_INDUSTRIES_TIME_SERIES_COLUMN_NAMES.index(TUPLE_INDUSTRIES_TIME_SERIES_INDUSTRIES[
                                                      _index_tuple.OPTION_NAME])
