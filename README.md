# NCI-Library-System

# PBI-01: User Registration and Login - Testing Plan & Scenarios

As part of Checkpoint 3 requirements, the User Registration and Login (PBI-01) have had some testing to validate the functions, data, and security.

## Test Scenarios & Cases

| Test ID | Task | Description | Expected Result | Status |
| **TC-01** | Database (T1) | Initialize SQLite database (`library.db`) via Flask application start. | The `users` table is successfully created with `id`, `username`, and `password` columns. | **Passed** |
| **TC-02** | Registration (T2) | Submit valid registration form (`/register`) with a new username and password. | User data is securely inserted into the SQLite database, and the user is redirected to the login page. | **Passed** |
| **TC-03** | Login View (T3) | Access the login page (`/login`) via GET request. | The HTML login form renders correctly, prompting for username and password credentials. | **Passed** |
| **TC-04** | User Validation (T4) | Submit correct credentials on the login form (`/login` via POST). | The system queries the database, verifies the match, creates a session, and grants access with a welcome message. | **Passed** |
| **TC-05** | Error Handling (T4) | Submit invalid or incorrect username/password combination. | The system rejects the entry and displays an error message ("Invalid username or password!"). | **Passed** |
