# Student Management System (SMS)

## 1. Introduction

The Student Management System (SMS) is a Python-based college project developed to manage student information through a computer application. The project started as a command-line program and is now being developed into a graphical application.

The application is intended to make common student-record operations easier to perform and maintain. Student information is currently stored in a JSON file.

## 2. Problem Statement

Student details need to be stored and retrieved accurately. Handling records manually or through disconnected files can make searching and updating information inconvenient. This project provides a structured application for performing basic student-record operations.

## 3. Project Objectives

- Create and maintain student records.
- Display and search for existing student information.
- Update student details when changes are required.
- Delete records when they are no longer needed.
- Store data so that it remains available after the application closes.
- Develop a graphical interface to make the application easier to use.
- Improve the project gradually through testing and modular development.

## 4. Technologies Used

| Technology | Use in the project |
|---|---|
| Python | Main programming language |
| JSON | Current student-record storage |
| Tkinter / CustomTkinter | GUI development |
| Git | Source-code version control |
| GitHub | Remote repository and project history |
| Visual Studio Code | Development environment |

The exact GUI library used by each screen should be kept consistent with the implementation as the interface develops.

## 5. Student Information

The current backend uses the following student fields:

| Field | Description |
|---|---|
| `Register_no` | Student registration number |
| `Name` | Student name |
| `Branch` | Student's academic branch |
| `Semister` | Semester (spelling used in the current code) |
| `phone_no` | Contact number |
| `Address` | Student address |

The registration number is intended to be the main identifier for locating a student record.

## 6. Implemented Work

The Python backend has been developed with basic CRUD operations:

- Insert a student record.
- View student records.
- Search for a student.
- Update student details.
- Delete a student record.
- Save and load student data using JSON.

The first version provided these operations through a command-line interface. The project now includes separate files for backend logic, login, dashboard, and authentication-related development.

## 7. Current Development Status

The project is transitioning from its original CLI implementation to a GUI-based application. The repository contains `Backend.py`, `login.py`, `Dashboard.py`, and `auth.py`, along with a `data` directory for JSON storage.

The presence of these files does not mean every screen or workflow is fully integrated. GUI completion and connection to backend operations remain part of the development work.

## 8. Future Scope

The following improvements are under consideration or planned:

- Complete the GUI and connect its screens to backend operations.
- Improve input validation and error handling.
- Introduce an HTTP/REST API, potentially using FastAPI.
- Evaluate moving from JSON storage to SQLite or PostgreSQL.
- Add PDF or Excel report export if it fits the final project requirements.
- Improve testing and technical documentation.

## 9. Project Information

- **Project:** Student Management System (SMS)
- **Developer:** Thangedupalli Mahesh
- **Programme:** Diploma in Computer Science and Engineering
- **Institution:** M.N. Technical Institute
- **Expected completion:** 2027

Review institution spelling and academic details before using this document for formal submission.
