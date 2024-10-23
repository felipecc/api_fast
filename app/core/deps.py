from contextlib import asynccontextmanager
from app.core.db_oracle import initialize_pool_cx_oracle, close_pool_cx_oracle,get_db_cx_oracle
from app.core.config import settings
import cx_Oracle

from fastapi import Depends, FastAPI
from typing import Annotated


ConnectionCxOracle = Annotated[cx_Oracle.Connection, Depends(get_db_cx_oracle)]

@asynccontextmanager
async def lifespan(app: FastAPI): # type: ignore
    initialize_pool_cx_oracle(user=settings.oracle_cx_user, password=settings.oracle_cx_pwd, dsn=settings.oracle_cx_dsn)
    yield
    close_pool_cx_oracle()
