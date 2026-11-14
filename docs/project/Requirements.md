# Student Management System — Requirements

> This is an initial working requirements document. Confirm each item against the final project scope before academic submission.

## 1. Functional Requirements

### Student records
- The application should allow a user to add a student record.
- The application should display stored student records.
- The application should search for a student using the registration number.
- The application should update an existing student record.
- The application should delete a student record.

### Data fields
A student record currently uses:
- Registration number (`Register_no`)
- Name (`Name`)
- Branch (`Branch`)
- Semester (`Semister`)
- Phone number (`phone_no`)
- Address (`Address`)

### Interface
- The project is being developed from a CLI program into a GUI application.
- Login and dashboard screens exist in the current development structure; their final behavior and access rules should be documented after implementation is complete.

## 2. Non-Functional Requirements
- Store records consistently and preserve them between program runs.
- Keep code organized into understandable modules.
- Validate user input before saving changes.
- Show useful messages when an operation succeeds or fails.
- Avoid committing real student personal information to a public repository.

## 3. Items to Confirm
- Exact user roles and permissions.
- Whether student/staff self-registration will be included.
- Final authentication and password-storage design.
- Whether the final storage will remain JSON or move to a database.
- Minimum supported Python version and operating system.
