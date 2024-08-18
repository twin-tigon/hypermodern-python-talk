from fastapi import APIRouter

from app.schemas import HealthCheck

router = APIRouter()


@router.get(
    "/",
    status_code=200,
    response_model=HealthCheck,
)
def read_health_check() -> HealthCheck:
    return HealthCheck(status="ok")
