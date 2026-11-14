# Student Management System (SMS)

## 1. Introduction
The Student Management System (SMS) is a college project intended to organize student information and make common student-record operations easier to perform.

The project began as a command-line (CLI) Python application. It is being developed into a graphical application with a more organized code structure.

## 2. Problem Statement
Managing student details manually or across separate files can make it harder to add, find, update, and remove records consistently. SMS aims to provide a single application for these basic student-record tasks.

## 3. Objectives
- Add and maintain student records.
- View and search student information.
- Update existing records.
- Delete records when required.
- Provide a graphical interface as development progresses.
- Keep application code and data files organized.

## 4. Current Technical Foundation
- Language: Python
- Current data storage: JSON file (`data/students.json`)
- Earlier interface: command-line interface
- Current interface work: Tkinter / CustomTkinter-based GUI
- Version control: Git and GitHub

## 5. Student Record Fields
The earlier backend uses these fields:
- `Register_no`
- `Name`
- `Branch`
- `Semister` (current code spelling)
- `phone_no`
- `Address`

## 6. Development Status
The Python backend has CRUD operations for inserting, viewing, searching, updating, and deleting student records. The project is being expanded with a GUI and separate login/dashboard modules.

This document describes the known project state at the time it was written. Update it as implementation changes.

## 7. Future Scope
Planned or considered improvements include:
- Complete and connect the GUI screens to the backend.
- Expose backend operations through an HTTP/REST API.
- Introduce a relational database such as SQLite or PostgreSQL.
- Improve validation, error handling, and project documentation.
- Add PDF/Excel export features if they remain in the project scope.

## 8. Project Owner
Add your preferred author name, institute details, and academic year before formal submission.
