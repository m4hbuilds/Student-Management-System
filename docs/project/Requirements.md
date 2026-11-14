# Student Management System — Requirements

## 1. Purpose

This document describes the main requirements for the Student Management System. It distinguishes the student-record functions already developed in the Python backend from interface and infrastructure work that is still being developed.

## 2. Functional Requirements

### 2.1 Student record management

The backend should support the following operations:

1. **Insert:** Add a student record containing registration number, name, branch, semester, phone number, and address.
2. **View:** Display the student records stored by the application.
3. **Search:** Find a student using the registration number.
4. **Update:** Modify the details of an existing student.
5. **Delete:** Remove a selected student record.

These CRUD operations have been implemented in the Python backend.

### 2.2 Data storage

- Student data is currently stored in `data/students.json`.
- The application should load saved records when required.
- Changes should be written back to the JSON file.
- Registration numbers should be treated as the main record identifier.

### 2.3 Graphical interface

The project is being developed with a graphical interface. The repository currently includes login and dashboard modules. The screens must be connected to the backend and tested before the GUI can be considered complete.

### 2.4 Authentication

The repository includes `auth.py` and `login.py` for authentication-related development. Final login rules, account creation, password handling, and role permissions must be confirmed and tested before being described as completed functionality.

## 3. Non-Functional Requirements

- **Usability:** The GUI should present student operations clearly.
- **Data consistency:** Record changes should be saved correctly.
- **Validation:** Required fields and registration numbers should be checked before saving.
- **Maintainability:** Interface, backend, and data-handling responsibilities should remain organized.
- **Reliability:** Errors such as missing records or invalid input should be handled with useful messages.
- **Privacy:** Real student personal information should not be committed to a public repository.

## 4. Current Student Record Fields

| Field | Requirement |
|---|---|
| Registration number | Identify a student record |
| Name | Store the student's name |
| Branch | Store the academic branch |
| Semester | Store the current semester |
| Phone number | Store as text to preserve formatting |
| Address | Store the student's address |

## 5. Future Requirements

The following are possible future improvements, not current completed features:

- Provide a REST API for student operations.
- Move data from JSON to a relational database.
- Add report generation in PDF or Excel format.
- Finalize role-based access for administrator, staff, and student users.
