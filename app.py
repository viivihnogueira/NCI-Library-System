import sqlite3

from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = "nci-library-secret-key"


# Creating the user database table
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


init_db()


# Home page routing
@app.route("/")
def home():
    return (
        'Welcome to NCI Library System! '
        'Go to <a href="/register">Register</a> '
        'or <a href="/login">Login</a>.'
    )


# Showing Register page (GET)
@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


# Saving Register data to database (POST)
@app.route("/register", methods=["POST"])
def register_user():
    username = request.form["username"].strip()
    password = request.form["password"].strip()

    if not username or not password:
        return (
            'Username and password are required. '
            '<a href="/register">Try again</a>'
        )

    try:
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    except sqlite3.IntegrityError:
        return (
            'Username already registered! '
            '<a href="/register">Try another username</a>'
        )


# Showing Login page (GET)
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


# Validating Login data (POST)
@app.route("/login", methods=["POST"])
def login_user():
    username = request.form["username"].strip()
    password = request.form["password"].strip()

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Checking if the username and password exist in the database
    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = ? AND password = ?
        """,
        (username, password),
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return (
            f"<h1>Welcome back, {username}!</h1>"
            "<p>Login successful.</p>"
            "<br>"
            "<a href='/login'>Logout</a>"
        )

    return (
        'Invalid username or password! '
        '<a href="/login">Try again</a>'
    )


if __name__ == "__main__":
    app.run(port=5000)
