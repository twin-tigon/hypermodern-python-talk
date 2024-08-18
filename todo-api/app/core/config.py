from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    PROJECT_NAME: str = "todo-api"
    ALLOWED_CORS_ORIGIN: str = "http://localhost"
    HTTP_HOST: str = "localhost"
    HTTP_PORT: int = 8000
    API_STR: str = "/api"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///data/local.db"


settings = Settings()
