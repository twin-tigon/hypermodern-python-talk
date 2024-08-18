from collections.abc import Generator

import pytest
from app.main import app
from app.models import Base
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session


@pytest.fixture
def engine() -> Generator[Engine, None, None]:
    engine = create_engine("sqlite:///data/test.db", echo=True)

    yield engine


@pytest.fixture
def init_db(engine: Engine) -> Generator[None, None, None]:
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(init_db, engine: Engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
