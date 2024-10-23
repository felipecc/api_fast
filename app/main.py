from fastapi import FastAPI
from app.core.config import settings
from app.routers.main import api_router
from app.core.deps import lifespan


app = FastAPI(title=settings.app_name,lifespan=lifespan)

app.include_router(api_router, prefix=settings.api_v1_str)
