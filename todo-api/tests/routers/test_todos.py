from app.core import settings
from app.repos import Todos
from fastapi.testclient import TestClient


def test_create_todo_ok(mocker, client: TestClient):
    mock_todo = {"id": 1, "title": "Mocked Todo"}
    mocker.patch.object(Todos, "create_todo", return_value=mock_todo)
    spy = mocker.spy(Todos, "create_todo")

    response = client.post(f"{settings.API_STR}/todos/", json="Mocked Todo")

    assert response.status_code == 200
    assert response.json() == mock_todo
    spy.assert_called_once_with("Mocked Todo")


def test_read_todo_ok(mocker, client: TestClient):
    mock_todo = {"id": 1, "title": "Mocked Todo"}
    mocker.patch.object(Todos, "read_todo", return_value=mock_todo)
    spy = mocker.spy(Todos, "read_todo")

    response = client.get(f"{settings.API_STR}/todos/1")

    assert response.status_code == 200
    assert response.json() == mock_todo
    spy.assert_called_once_with(1)


def test_read_todo_nok(mocker, client: TestClient):
    mocker.patch.object(
        Todos, "read_todo", side_effect=ValueError("Todo with id 1 not found")
    )
    spy = mocker.spy(Todos, "read_todo")

    response = client.get(f"{settings.API_STR}/todos/1")

    assert response.status_code == 404
    spy.assert_called_once_with(1)


def test_update_todo_ok(mocker, client: TestClient):
    mock_todo = {"id": 1, "title": "Updated Mocked Todo"}
    mocker.patch.object(Todos, "update_todo", return_value=mock_todo)
    spy = mocker.spy(Todos, "update_todo")

    response = client.patch(f"{settings.API_STR}/todos/1", json="Updated Mocked Todo")

    assert response.status_code == 200
    assert response.json() == mock_todo
    spy.assert_called_once_with(1, "Updated Mocked Todo")


def test_update_todo_nok(mocker, client: TestClient):
    mocker.patch.object(
        Todos, "update_todo", side_effect=ValueError("Todo with id 1 not found")
    )
    spy = mocker.spy(Todos, "update_todo")

    response = client.patch(f"{settings.API_STR}/todos/1", json="Updated Mocked Todo")

    assert response.status_code == 404
    spy.assert_called_once_with(1, "Updated Mocked Todo")


def test_delete_todo_ok(mocker, client: TestClient):
    mocker.patch.object(Todos, "delete_todo", return_value=None)
    spy = mocker.spy(Todos, "delete_todo")

    response = client.delete(f"{settings.API_STR}/todos/1")

    assert response.status_code == 200
    assert response.json() is None
    spy.assert_called_once_with(1)


def test_delete_todo_nok(mocker, client: TestClient):
    mocker.patch.object(
        Todos, "delete_todo", side_effect=ValueError("Todo with id 1 not found")
    )
    spy = mocker.spy(Todos, "delete_todo")

    response = client.delete(f"{settings.API_STR}/todos/1")

    assert response.status_code == 404
    spy.assert_called_once_with(1)


def test_read_todos_ok(mocker, client: TestClient):
    mock_todos = [
        {"id": 1, "title": "Mocked Todo 1"},
        {"id": 2, "title": "Mocked Todo 2"},
    ]
    mocker.patch.object(Todos, "read_todos", return_value=mock_todos)
    spy = mocker.spy(Todos, "read_todos")

    response = client.get(f"{settings.API_STR}/todos/")

    assert response.status_code == 200
    assert response.json() == mock_todos
    spy.assert_called()
