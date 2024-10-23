from fastapi import APIRouter
from app.routers.atendimento import controller_atendimento

api_router = APIRouter()

api_router.include_router(controller_atendimento.router,tags=['atendimento'])
