from fastapi import APIRouter

from app.routers.health_check import router as health_check_router
from app.routers.todos import router as todos_router

router = APIRouter()
router.include_router(health_check_router, tags=["health_check"])
router.include_router(todos_router, tags=["todos"])
