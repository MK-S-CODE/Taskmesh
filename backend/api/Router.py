from fastapi import APIRouter
from api.health.router import health_router

api_router = APIRouter()

api_router.include_router(health_router)