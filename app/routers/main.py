from fastapi import APIRouter
from app.routers.atendimento import route_atendimento

api_router = APIRouter()

api_router.include_router(route_atendimento.router,tags=['atendimento'])
