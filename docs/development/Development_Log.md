# Development Log

This document records the development journey of the Student Management System, from the first command-line version to the current GUI development.

## Milestone 1 — First CLI Application

**Goal:** Build an initial Student Management System in Python and practise basic student-record operations.

**Work completed:**
- Created the first command-line version of the project.
- Added menu-driven student-record operations.
- Started implementing CRUD functionality for student details.

**Challenges and lessons:**
- Practised organizing a Python program around separate operations.
- Learned how to accept and process user input.
- Built an initial understanding of how a student record can be represented in Python.

**Next step:** Improve record handling and introduce persistent storage.

## Milestone 2 — JSON-Based Backend

**Goal:** Save student records so they remain available after the program closes.

**Work completed:**
- Used JSON to store student records in `students.json`.
- Implemented JSON loading and saving in the backend.
- Developed insert, view, search, update, and delete operations.
- Used registration number as the main search identifier.

**Challenges and lessons:**
- Practised reading and writing files with Python.
- Fixed a file-opening mode issue during JSON saving.
- Learned how to convert between Python data and JSON data.

**Next step:** Keep backend logic organized and begin developing a graphical interface.

## Milestone 3 — Python Experiments

**Goal:** Test small Python ideas and validation logic that could support the main application.

**Work completed:**
- Created separate experimental scripts in the `experiments/` folder.
- Worked on small exercises involving names, gender validation, and OTP-related logic.
- Kept practice code separate from the main application modules.

**Challenges and lessons:**
- Used small programs to test ideas before considering their use in the main project.
- Practised breaking a larger learning task into smaller experiments.

**Next step:** Retain useful experiments and move suitable, tested logic into the main application only when needed.

## Milestone 4 — GUI Development Started

**Goal:** Move the project from a command-line workflow toward a graphical application.

**Work completed:**
- Started separating GUI-related code into its own files.
- Added `login.py` for login-screen development.
- Added `Dashboard.py` for dashboard development.
- Added `auth.py` for authentication-related logic.
- Continued keeping backend operations in `Backend.py`.

**Challenges and lessons:**
- Began learning how GUI screens and backend functions should work together.
- Identified the need to keep interface code separate from data operations.

**Next step:** Complete the screens and connect their actions to the backend.

## How to Add Future Entries

For each new milestone, add a dated section with the actual work completed, problems encountered, and the next task. Do not mark a feature as complete until it has been implemented and tested.
