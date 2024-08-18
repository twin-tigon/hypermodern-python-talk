from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.db import get_session
from app.repos import Todos

SessionDep = Annotated[Session, Depends(get_session)]


def get_todos_repo(session: SessionDep) -> Todos:
    todos_repo = Todos(session)

    return todos_repo


TodosRepoDep = Annotated[Todos, Depends(get_todos_repo)]
