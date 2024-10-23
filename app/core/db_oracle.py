from contextlib import contextmanager
from typing import Any, Dict, Generator, List, Union

# Import both cx_Oracle and oracledb
import cx_Oracle
import oracledb


@contextmanager
def create_cx_oracle_connection(
    *, user: str, password: str, dsn: str
) -> Generator[cx_Oracle.Connection, None, None]:
    """
    Create a connection to the Oracle database using cx_Oracle.

    :param user: Database user
    :param password: Database password
    :param dsn: Data Source Name
    :return: Connection object
    """
    connection = None
    try:
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
        yield connection
    except cx_Oracle.Error as e:
        print(f"Error connecting to Oracle Database (cx_Oracle): {e}")
    finally:
        if connection:
            connection.close()

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
        # Inicializa o cursor
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
        # Verifica se o cursor foi inicializado antes de tentar fechá-lo
        if cursor:
            cursor.close()
