from fastapi import APIRouter
from app.routers.atendimento import router_atendimento

api_router = APIRouter()

api_router.include_router(router_atendimento.router, tags=["atendimento"])
