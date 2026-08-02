"""myUpdateManagerDefinitions.py."""

__title__: str = "myUpdateManagerDefinitions"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

from mydatabase.mySQLDataBase import STR_SQL_DATA_BASE_NAME, STR_SQL_DATA_DIR_NAME
from mytuple import myTuple

STR_DATA_BASE_FILE_NAME: str = STR_SQL_DATA_BASE_NAME

STR_DATA_BASE_DIR_NAME: str = STR_SQL_DATA_DIR_NAME

STR_DATA_BASE_TABLE_NAME: str = 'update_manager'

STR_DATA_BASE_SCHEMA_NAME: str = 'main'

DATA_BASE_TIMEOUT: float = 5.0

DATA_BASE_CONNECTION_URI: bool = True

TUPLE_UPDATE_MANAGER_DATE: tuple[str, str, tuple[str, str, str, str], type[tuple]] = \
    ('UPDATE_MANAGER.DATE',
    'date',
    ('date', 'TEXT', 'NOT NULL', 'PRIMARY KEY'),
    tuple)

_index_tuple = myTuple.MyTuple

LIST_UPDATE_MANAGER_COLUMN_NAMES: list[str] = [TUPLE_UPDATE_MANAGER_DATE[
                                                      _index_tuple.OPTION_NAME]]

INDEX_PRIMARY_KEY = LIST_UPDATE_MANAGER_COLUMN_NAMES.index(TUPLE_UPDATE_MANAGER_DATE[
                                                      _index_tuple.OPTION_NAME])
