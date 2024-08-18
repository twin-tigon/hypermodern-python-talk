from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas


class Todos:
    def __init__(self, session: Session) -> None:
        self._session = session

    def _get_todo(self, id: int) -> models.Todo:
        stmt = select(models.Todo).where(models.Todo.id == id)
        result = self._session.scalar(stmt)
        if result is None:
            raise ValueError(f"Todo with id {id} not found")

        return result

    def _convert_model_to_schema(self, model: models.Todo) -> schemas.Todo:
        return schemas.Todo(
            id=model.id,
            title=model.title,
        )

    def create_todo(self, title: str) -> schemas.Todo:
        todo = models.Todo(
            title=title,
        )

        self._session.add(todo)
        self._session.commit()

        return self._convert_model_to_schema(todo)

    def read_todo(self, id: int) -> schemas.Todo:
        todo = self._get_todo(id)

        return self._convert_model_to_schema(todo)

    def update_todo(self, id: int, title: str) -> schemas.Todo:
        todo = self._get_todo(id)
        todo.title = title

        self._session.add(todo)
        self._session.commit()

        return self._convert_model_to_schema(todo)

    def delete_todo(self, id: int) -> None:
        todo = self._get_todo(id)

        self._session.delete(todo)
        self._session.commit()

    def read_todos(self) -> list[schemas.Todo]:
        stmt = select(models.Todo)
        result = self._session.scalars(stmt)

        return [self._convert_model_to_schema(todo) for todo in result]
