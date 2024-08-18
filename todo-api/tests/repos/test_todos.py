from collections.abc import Generator

import pytest
from app.repos import Todos
from app.schemas import Todo
from sqlalchemy.orm import Session


@pytest.fixture
def todos_repo(session: Session) -> Generator[Todos, None, None]:
    todos_repo = Todos(session)

    yield todos_repo


def test_create_todo_ok(todos_repo: Todos) -> None:
    todo = todos_repo.create_todo("My todo")

    assert todo == Todo(id=1, title="My todo")

    todos_repo.delete_todo(1)


def test_read_todo_ok(todos_repo: Todos) -> None:
    todos_repo.create_todo("My todo")
    todo = todos_repo.read_todo(1)

    assert todo == Todo(id=1, title="My todo")

    todos_repo.delete_todo(1)


def test_update_todo_ok(todos_repo: Todos) -> None:
    todos_repo.create_todo("My todo")
    todo = todos_repo.update_todo(1, "My updated todo")

    assert todo == Todo(id=1, title="My updated todo")

    todos_repo.delete_todo(1)


def test_delete_todo_ok(todos_repo: Todos) -> None:
    todo = todos_repo.create_todo("My todo")

    assert todos_repo.read_todo(todo.id) == Todo(id=todo.id, title="My todo")

    todos_repo.delete_todo(todo.id)

    with pytest.raises(ValueError):
        todos_repo.read_todo(todo.id)


def test_read_todos_ok(todos_repo: Todos) -> None:
    for title in ["First todo", "Second todo", "Third todo"]:
        todos_repo.create_todo(title)

    expected_todos = [
        Todo(id=1, title="First todo"),
        Todo(id=2, title="Second todo"),
        Todo(id=3, title="Third todo"),
    ]
    todos = todos_repo.read_todos()

    assert todos == expected_todos

    for todo in expected_todos:
        todos_repo.delete_todo(todo.id)

    todos = todos_repo.read_todos()
    assert todos == []
