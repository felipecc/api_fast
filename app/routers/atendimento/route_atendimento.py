from fastapi import APIRouter
from typing import Any
from app.core.deps import ConnectionCxOracle
from app.services.atendimento.service_atendimento import ServiceAtendimento

router = APIRouter()

@router.get("/atendimentos")
def get_atendimentos(connection: ConnectionCxOracle) -> Any: # type: ignore
    service_atendimento = ServiceAtendimento(connection=connection)
    return service_atendimento.get_atendimentos()

