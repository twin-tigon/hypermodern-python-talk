from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core import settings
from app.routers import router

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_CORS_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.API_STR)


def start() -> None:
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HTTP_HOST,
        port=settings.HTTP_PORT,
        reload=True,
    )


if __name__ == "__main__":
    start()
