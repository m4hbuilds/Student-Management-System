# Student Management System — Development Roadmap

This roadmap reflects the project's current direction. Items are marked according to the work known to be completed or still planned.

## Phase 1 — CLI and Backend Foundation

- [x] Create the first command-line Student Management System.
- [x] Implement student insertion and viewing.
- [x] Implement student search, update, and delete operations.
- [x] Save and load student records using JSON.
- [x] Use registration number as the main search identifier.

## Phase 2 — Experiments and Code Organization

- [x] Keep Python experiments in a separate `experiments/` folder.
- [x] Create separate application modules for backend, login, dashboard, and authentication-related work.
- [ ] Review experimental scripts and document which ideas are adopted by the main application.

## Phase 3 — GUI Development

- [x] Start GUI development.
- [x] Create the login and dashboard module files.
- [ ] Complete the login screen workflow.
- [ ] Complete the dashboard interface.
- [ ] Connect GUI actions to backend CRUD operations.
- [ ] Test all CRUD operations through the GUI.
- [ ] Improve validation and user-facing error messages.

## Phase 4 — Project Quality

- [ ] Test normal and invalid input cases.
- [ ] Check duplicate registration-number handling.
- [ ] Add safe sample data for demonstrations.
- [ ] Keep README and technical documentation up to date.
- [ ] Capture screenshots of completed application features.

## Phase 5 — API Development (Future)

- [ ] Learn HTTP methods and REST API concepts.
- [ ] Design endpoints for student-record operations.
- [ ] Build an API service using FastAPI.
- [ ] Test API requests and responses.
- [ ] Evaluate whether the GUI should communicate with the backend through the API.

## Phase 6 — Database (Future)

- [ ] Compare JSON storage with relational database storage.
- [ ] Design a student table and define a primary key.
- [ ] Evaluate SQLite and PostgreSQL.
- [ ] Migrate sample records and test CRUD operations.

## Possible Enhancements

- [ ] PDF and Excel report export.
- [ ] Finalize administrator, staff, and student roles.
- [ ] Improve reports and dashboard summaries.

Future items should be moved to the completed section only after implementation and testing.
