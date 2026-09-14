from typing import List
from .models import TodoItem

# Simple in-memory store
_todos: List[TodoItem] = []
_next_id = 1

def get_todos() -> List[TodoItem]:
    return _todos.copy()

def add_todo(item: TodoItem) -> TodoItem:
    global _next_id
    item.id = _next_id
    _next_id += 1
    _todos.append(item)
    return item

def delete_todo(todo_id: int) -> None:
    global _todos
    for i, todo in enumerate(_todos):
        if todo.id == todo_id:
            del _todos[i]
            return
    raise ValueError(f"Todo with id {todo_id} not found")
