# System Architecture

## 1. Current High-Level Design

The project currently has a Python application layer and JSON-based file storage.

```text
User
  |
  v
GUI screens (login / dashboard — under development)
  |
  v
Python backend (student CRUD operations)
  |
  v
JSON storage (data/students.json)
```

The original version used a command-line interface. The current work separates interface files and backend logic.

## 2. Known Project Modules

| Path | Current purpose |
|---|---|
| `Backend.py` | Student CRUD and data handling |
| `login.py` | Login interface |
| `Dashboard.py` | Dashboard interface |
| `auth.py` | Authentication-related logic |
| `data/students.json` | JSON student-record storage |
| `experiments/` | Earlier CLI code and Python experiments |

These descriptions reflect the project structure discussed during development. Update them if module responsibilities change.

## 3. Current Data Flow
1. A user initiates an operation through the application.
2. The relevant Python logic handles the request.
3. The backend reads or updates the JSON data.
4. The application displays the result.

## 4. Planned Evolution
A possible future architecture is:

```text
GUI
 |
 v
HTTP/REST API (planned)
 |
 v
Python API service (e.g. FastAPI — planned)
 |
 v
Database (SQLite or PostgreSQL — planned)
```

The API and database layers are future plans, not claims about the current implementation.
