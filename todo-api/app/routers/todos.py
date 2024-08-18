from typing import Annotated, Any

from fastapi import APIRouter, Body, HTTPException, status

from app.core import TodosRepoDep
from app.schemas import Todo

router = APIRouter(prefix="/todos")


@router.post("/", status_code=200, response_model=Todo)
async def create_todo(todos_repo: TodosRepoDep, title: Annotated[str, Body()]) -> Any:
    return todos_repo.create_todo(title)


@router.get(
    "/{id}",
    status_code=200,
    response_model=Todo,
)
async def read_todo(todos_repo: TodosRepoDep, id: int) -> Any:
    try:
        todo = todos_repo.read_todo(id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise (e)

    return todo


@router.patch("/{id}", status_code=200, response_model=Todo)
async def update_todo(
    todos_repo: TodosRepoDep, id: int, title: Annotated[str, Body()]
) -> Any:
    try:
        todo = todos_repo.update_todo(id, title)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise (e)

    return todo


@router.delete("/{id}", status_code=200)
async def delete_todo(todos_repo: TodosRepoDep, id: int) -> Any:
    try:
        todo = todos_repo.delete_todo(id)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        raise (e)

    return todo


@router.get(
    "/",
    status_code=200,
    response_model=list[Todo],
)
async def read_todos(todos_repo: TodosRepoDep) -> Any:
    return todos_repo.read_todos()
