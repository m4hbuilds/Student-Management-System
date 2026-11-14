# System Architecture

## 1. Current Architecture

The project currently uses Python for application logic and a JSON file for student-record storage. It began as a command-line application. GUI development is now organized into separate modules.

```text
                 User
                  |
                  v
       GUI development modules
       login.py / Dashboard.py
                  |
                  v
          Python backend
             Backend.py
                  |
                  v
          JSON data storage
        data/students.json
```

This diagram represents the intended connection between the current modules. The GUI-to-backend integration should be verified as development continues.

## 2. Main Project Components

| Component | Responsibility |
|---|---|
| `Backend.py` | Student CRUD and data operations |
| `login.py` | Login screen development |
| `Dashboard.py` | Dashboard screen development |
| `auth.py` | Authentication-related logic |
| `data/students.json` | Current student data file |
| `experiments/` | Earlier CLI program and Python experiments |
| `docs/` | Project documentation |

## 3. Data Flow

The backend data flow for a student operation is:

1. The application requests an operation, such as adding or searching for a student.
2. Python backend logic processes the operation.
3. The backend reads from or writes to `data/students.json`.
4. The operation result is returned to the calling part of the application.

## 4. Current Storage Design

JSON is used for persistence at this stage. It keeps the initial project simple and allows the student records to be saved in a readable file.

The current storage approach is suitable for the project's learning and early development stage. A relational database may be considered later as requirements grow.

## 5. Planned Architecture Improvements

A possible later design is:

```text
GUI
 |
 v
HTTP / REST API
 |
 v
Python API service (FastAPI)
 |
 v
Relational database (SQLite or PostgreSQL)
```

This is a future architecture direction. The REST API and relational database are not represented as implemented parts of the current application.
