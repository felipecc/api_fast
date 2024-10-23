from contextlib import contextmanager
from typing import Any, Dict, Generator, List, Union

# Import both cx_Oracle and oracledb
import cx_Oracle
import oracledb


pool_oracle: cx_Oracle.SessionPool


def initialize_pool_cx_oracle(
    *,
    user: str,
    password: str,
    dsn: str,
    min: int = 1,
    max: int = 5,
    increment: int = 1,
) -> None:    
    global pool_oracle
    pool_oracle = cx_Oracle.SessionPool(
        user=user,
        password=password,
        dsn=dsn,
        min=min,
        max=max,
        increment=increment,
        threaded=True,
        getmode=cx_Oracle.SPOOL_ATTRVAL_NOWAIT,
    )

def close_pool_cx_oracle() -> None:
    
    global pool_oracle
    if pool_oracle:
        pool_oracle.close()



@contextmanager
def get_cx_oracle_connection_pool() -> Generator[cx_Oracle.Connection, None, None]:
    connection = None    
    global pool_oracle
    
    if not pool_oracle:
      raise RuntimeError("Database pool is not initialized")

    try:
        connection = pool_oracle.acquire()
        yield connection
    except cx_Oracle.Error as e:
        print(f"Error getting connect from Oracle Database (cx_Oracle): {e}")
    finally:
        if connection:
            pool_oracle.release(connection)


def get_db_cx_oracle() -> Generator[cx_Oracle.Connection, None, None]:
    with get_cx_oracle_connection_pool() as connection:
        yield connection            


@contextmanager
def create_oracledb_connection(
    *, user: str, password: str, dsn: str
) -> Generator[oracledb.Connection, None, None]:
    """
    Create a connection to the Oracle database using oracledb.

    :param user: Database user
    :param password: Database password
    :param dsn: Data Source Name
    :return: Connection object
    """
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        yield connection
    except oracledb.Error as e:
        print(f"Error connecting to Oracle Database (oracledb): {e}")
        return None
    finally:
        if connection:
            connection.close()


def execute_query(
    connection: Union[cx_Oracle.Connection, oracledb.Connection],
    query: str,
    params: Dict[str, Any] | None = None,
) -> List | None:
    if not connection:
        raise Exception("Connection is none")

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(query, params or {})
        cursor.rowfactory = lambda *args: dict(
            zip([str.lower(d[0]) for d in cursor.description], args)
        )
        results = cursor.fetchall()
        return results
    except (cx_Oracle.Error, oracledb.Error) as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
