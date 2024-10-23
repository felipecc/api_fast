from typing import List
from fastapi.templating import Jinja2Templates
import os
from app.models.atendimento import Atendimento
from app.services.atendimento.interfaces.service_atendimento_interface import (
    ServiceAtendimentoInterface,
)
import cx_Oracle
from app.core.db_oracle import execute_query


DIR_BASE = os.path.abspath(os.path.join(__file__, "../"))

class ServiceAtendimento(ServiceAtendimentoInterface):
    def __init__(self, connection: cx_Oracle.Connection) -> None:
        self.__connection = connection
        self.__templates = Jinja2Templates(directory=f"{DIR_BASE}/querys")


    def get_atendimentos(self) -> List[Atendimento] | None:
        query = self.__templates.get_template('atendimentos.sql')
        results = execute_query(connection=self.__connection, query=query.render())
        
        if not results:
            return None
        
        return [Atendimento(**result) for result in results]
        
