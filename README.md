# TodoStream – FastAPI + Streamlit Todo App

## Overview
A simple **intermediate‑level** demonstration of a full‑stack web app built with:
- **FastAPI** – backend REST API (served by **uvicorn**) providing CRUD operations for a Todo list.
- **Streamlit** – lightweight frontend UI that consumes the API.
- **Docker / docker‑compose** – containerises both services and wires them together.

The app lets you **view**, **add**, and **delete** todo items.

## Project Structure
```
One_credit/
├── app/                     # FastAPI package
│   ├── __init__.py
│   ├── main.py               # FastAPI entry point
│   ├── models.py             # Pydantic Todo model
│   └── crud.py               # In‑memory data store
├── streamlit_app.py           # Streamlit UI
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Build image for both services
├── docker-compose.yml         # Run API and UI containers
└── README.md                  # This file
```

## Getting Started
1. **Prerequisites** – Install Docker and Docker‑Compose.
2. **Run the app**:
   ```bash
   cd /Users/gogulpranav/Documents/Projects/One_credit
   docker compose up --build
   ```
3. Open your browser:
   - FastAPI docs: <http://localhost:8000/docs>
   - Streamlit UI: <http://localhost:8501>

## How It Works
- **FastAPI** exposes three endpoints:
  - `GET /todos` – list all todos.
  - `POST /todos` – create a new todo.
  - `DELETE /todos/{id}` – delete a todo.
- **Streamlit** uses `requests` to call those endpoints, displaying the list and offering a form to add new items.

## Extending the Project
- Replace the in‑memory store with a real database (SQLite, Postgres, etc.).
- Add authentication (OAuth2/JWT) to protect the API.
- Split the Dockerfile into separate images for API and UI.
- Add unit tests with `pytest` and CI pipelines.

---
*Created for an inter‑college level submission.*
