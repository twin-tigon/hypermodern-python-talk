from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
