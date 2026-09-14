from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from .models import TodoItem
from .crud import get_todos, add_todo, delete_todo

app = FastAPI(title="Todo API")

@app.get("/todos", response_model=List[TodoItem])
async def read_todos():
    return get_todos()

@app.post("/todos", response_model=TodoItem)
async def create_todo(item: TodoItem):
    return add_todo(item)

@app.delete("/todos/{todo_id}")
async def remove_todo(todo_id: int):
    try:
        delete_todo(todo_id)
        return {"detail": "Todo deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
