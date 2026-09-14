import streamlit as st
import requests
import os
from typing import List, Dict

API_URL = os.getenv("API_URL", "http://api:8000")

st.title("Todo List App")

# Fetch todos

def fetch_todos() -> List[Dict]:
    try:
        resp = requests.get(f"{API_URL}/todos")
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        st.error(f"Failed to load todos: {e}")
        return []

# Add a new todo

def add_todo(title: str):
    payload = {"title": title, "completed": False}
    try:
        resp = requests.post(f"{API_URL}/todos", json=payload)
        resp.raise_for_status()
        st.success("Todo added")
    except Exception as e:
        st.error(f"Failed to add todo: {e}")

# Delete a todo by id

def delete_todo(todo_id: int):
    try:
        resp = requests.delete(f"{API_URL}/todos/{todo_id}")
        if resp.status_code == 200:
            st.success("Todo deleted")
        else:
            st.error(f"Delete failed: {resp.text}")
    except Exception as e:
        st.error(f"Failed to delete todo: {e}")

# Display current todos
todos = fetch_todos()
if todos:
    for todo in todos:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{todo['id']}. {todo['title']}")
        with col2:
            if st.button("Delete", key=todo['id']):
                delete_todo(todo['id'])
                st.experimental_rerun()
else:
    st.info("No todos yet!")

# Form to add a new todo
with st.form("add_todo"):
    new_title = st.text_input("Todo title")
    submitted = st.form_submit_button("Add")
    if submitted and new_title:
        add_todo(new_title)
        st.experimental_rerun()
