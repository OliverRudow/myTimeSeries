"""myScoresTimeSeriesDefinitions.py."""

__title__: str = "myScoresTimeSeriesDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'scores_time_series'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

DATA_BASE_INT_NUMBER_PRECEDED_DATA = 20


LIST_SECTIONS_WATCH_LIST: list[str] = ['SCORES_TIME_SERIES.QUOTE_ISIN',
                                       'SCORES_TIME_SERIES.ANALYST_SCORE',
                                       'SCORES_TIME_SERIES.DERIVATE_SCORE',
                                       'SCORES_TIME_SERIES.FUNDAMENTALS_SCORE',
                                       'SCORES_TIME_SERIES.PERFORMANCE_SCORE',
                                       'SCORES_TIME_SERIES.OVERALL_SCORE']

TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('SCORES_TIME_SERIES.QUOTE_ISIN',
    'quote_isin',
    ('quote_isin', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

TUPLE_SCORES_TIME_SERIES_ANALYST_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORES_TIME_SERIES.ANALYST_SCORE',
     'analyst_score',
    ('analyst_score', 'BLOB'),
    tuple)

TUPLE_SCORES_TIME_SERIES_DERIVATE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORES_TIME_SERIES.DERIVATE_SCORE',
     'derivate_score',
    ('derivate_score', 'BLOB'),
    tuple)

TUPLE_SCORES_TIME_SERIES_FUNDAMENTALS_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORES_TIME_SERIES.FUNDAMENTALS_SCORE',
    'fundamentals_score',
    ('fundamentals_score', 'BLOB'),
    tuple)

TUPLE_SCORES_TIME_SERIES_PERFORMANCE_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORES_TIME_SERIES.PERFORMANCE_SCORE',
    'performance_score',
    ('performance_score', 'BLOB'),
    tuple)

TUPLE_SCORES_TIME_SERIES_OVERALL_SCORE: tuple[str, str, tuple[str, str], type[tuple]] = \
    ('SCORES_TIME_SERIES.OVERALL_SCORE',
    'overall_score',
    ('overall_score', 'BLOB'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_SCORES_TIME_SERIES_COLUMN_NAMES: list[str] = [TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME],
                                                    TUPLE_SCORES_TIME_SERIES_ANALYST_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                    TUPLE_SCORES_TIME_SERIES_DERIVATE_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                    TUPLE_SCORES_TIME_SERIES_FUNDAMENTALS_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                    TUPLE_SCORES_TIME_SERIES_PERFORMANCE_SCORE[
                                                      _index_tuple.OPTION_NAME],
                                                    TUPLE_SCORES_TIME_SERIES_OVERALL_SCORE[
                                                      _index_tuple.OPTION_NAME]]

INDEX_PRIMARY_KEY = LIST_SCORES_TIME_SERIES_COLUMN_NAMES.index(TUPLE_SCORES_TIME_SERIES_QUOTE_ISIN[
                                                      _index_tuple.OPTION_NAME])
