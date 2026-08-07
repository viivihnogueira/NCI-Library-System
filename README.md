# NCI Library System

The NCI Library System is a web-based prototype developed for the Software Engineering CA2 project at the National College of Ireland.

The application allows users to register, log in and search the library catalogue by book title, author or category.

## Team Members

- Matheus Pinheiro — PBI-02: Book Search
- Viviani Nogueira Rabello — PBI-01: User Registration and Login

## Implemented Features

### PBI-01: User Registration and Login

- Register a new user.
- Store user details in an SQLite database.
- Prevent duplicate usernames.
- Log in using registered credentials.
- Reject incorrect credentials.
- Maintain the authenticated user through a Flask session.
- Protect pages that require authentication.
- Log out and clear the user session.

### PBI-02: Book Search

- Create and initialise the library book catalogue.
- Add sample books automatically.
- Search books by title.
- Search books by author.
- Search books by category.
- Support partial and case-insensitive search terms.
- Display book title, author, category and availability.
- Display a message when no matching books are found.
- Restrict the search page to authenticated users.

## Technologies

- Python
- Flask
- SQLite
- HTML
- Git and GitHub

## Project Structure

```text
NCI-Library-System/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
    ├── home.html
    ├── login.html
    ├── register.html
    └── search.html
```

The `library.db` database is created automatically when the application starts. It is not stored in the GitHub repository.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/viivihnogueira/NCI-Library-System.git
```

Open the project folder:

```bash
cd NCI-Library-System
```

### 2. Create a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependency

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open the following address in a web browser:

```text
http://127.0.0.1:5000
```

To stop the application, press `Control + C` in the terminal.

## How to Use the System

1. Open the registration page.
2. Create a username and password.
3. Log in using the registered credentials.
4. Open the Book Search page from the home page.
5. Enter a title, author or category.
6. Review the matching books and their availability.
7. Use the Logout link to end the session.

## Application Routes

| Route       | Purpose                               | Authentication Required |
| ----------- | ------------------------------------- | ----------------------: |
| `/register` | Register a user                       |                      No |
| `/login`    | Log in                                |                      No |
| `/`         | Display the home page                 |                     Yes |
| `/search`   | Search the book catalogue             |                     Yes |
| `/logout`   | Clear the session and return to login |                     Yes |

## Test Scenarios

| Test ID | Component      | Test                                  | Expected Result                                     | Status |
| ------- | -------------- | ------------------------------------- | --------------------------------------------------- | ------ |
| TC-01   | Database       | Start the Flask application           | The `users` and `books` tables are created          | Passed |
| TC-02   | Registration   | Register a new username and password  | The user is added and redirected to login           | Passed |
| TC-03   | Registration   | Register an existing username         | The duplicate username is rejected                  | Passed |
| TC-04   | Login          | Submit correct credentials            | The user session is created and the home page opens | Passed |
| TC-05   | Login          | Submit incorrect credentials          | An invalid credentials message is displayed         | Passed |
| TC-06   | Session        | Access the home page without login    | The user is redirected to login                     | Passed |
| TC-07   | Book Search    | Search by title                       | Matching books are displayed                        | Passed |
| TC-08   | Book Search    | Search by author                      | Books by the matching author are displayed          | Passed |
| TC-09   | Book Search    | Search by category                    | Books in the matching category are displayed        | Passed |
| TC-10   | Book Search    | Search using a partial lowercase term | Matching books are displayed                        | Passed |
| TC-11   | Book Search    | Search for a term that does not exist | A no-results message is displayed                   | Passed |
| TC-12   | Access Control | Access `/search` without login        | The user is redirected to login                     | Passed |
| TC-13   | Logout         | Log out and access a protected page   | The session is cleared and login is required        | Passed |

## GitHub Workflow

The project uses the following branch structure:

- `main` — final stable version.
- `development` — integration and testing version.
- `feature-login` — PBI-01 development.
- `feature-search-book` — PBI-02 development.
- `feature-documentation` — README and final documentation updates.

Feature branches are reviewed and merged into `development`. After final testing, `development` is merged into `main`.

## Current Limitations

- The project is an academic prototype intended for local demonstration.
- Passwords are stored directly in the SQLite database and are not hashed.
- The current prototype implements registration, login and book search only.
- The catalogue contains sample data created when the database is first initialised.
- Administrative, rental and purchasing functionality is outside the implemented sprint scope.
