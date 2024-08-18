from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
