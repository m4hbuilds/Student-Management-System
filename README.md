# Student Management System (V1)

A modular desktop Student Management System built with Python, Tkinter/CustomTkinter, and JSON storage. Designed with separation of concerns between authentication, GUI views, and local CRUD data operations.

## Features

- **Authentication Gate:** Decoupled login validation (`auth.py`) protecting access to the main dashboard.
- **Student Record Management (CRUD):** Add, view, update, and delete student records stored in structured JSON format (`Backend.py`).
- **Modular Project Structure:** Separates core application logic, persistent data files, and standalone validation prototypes (`experiments/`).

## Repository Structure

```text
Student-Management-System/
├── auth.py              # Credential validation logic
├── Backend.py           # JSON-based CRUD operations and data handling
├── Dashboard.py         # Main student management GUI
├── login.py             # Application entry point and login interface
├── data/
│   └── students.json    # Local student records storage (dummy data)
├── experiments/         # Early input validation and logic prototypes
│   ├── gender.py
│   ├── name.py
│   ├── otp.py
│   ├── p1.py
│   └── sample.py
├── docs/                # Project documentation and synopsis
├── screenshots/         # Application UI previews
├── LICENSE
├── README.md
└── requirements.txt