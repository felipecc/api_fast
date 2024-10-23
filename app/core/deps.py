from collections.abc import Generator
from app.core.db_oracle import create_cx_oracle_connection, create_oracledb_connection
from app.core.config import settings
import cx_Oracle
import oracledb
from fastapi import Depends
from typing import Annotated, Any


def get_db_oracledb() -> Generator[oracledb.Connection, None, None]:
    with create_oracledb_connection(
        user=settings.oracle_db_user,
        password=settings.oracle_db_pwd,
        dsn=settings.oracle_db_dsn,
    ) as connection:
        yield connection


def get_db_cx_oracle() -> Any :  # type: ignore # noqa: F821
    with create_cx_oracle_connection(
        user=settings.oracle_cx_user,
        password=settings.oracle_cx_pwd,
        dsn=settings.oracle_cx_dsn) as connection:
        yield connection
    

ConnectionCxOracle = Annotated[cx_Oracle.Connection, Depends(get_db_cx_oracle)]
