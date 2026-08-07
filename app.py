from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'nci-library-secret-key'


def init_db():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


init_db()


@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template(
        'home.html',
        username=session['username']
    )


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username'].strip()
    password = request.form['password'].strip()

    if not username or not password:
        return 'Username and password are required. <a href="/register">Try again</a>'

    try:
        conn = sqlite3.connect('library.db')
        c = conn.cursor()

        c.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)',
            (username, password)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    except sqlite3.IntegrityError:
        return 'Username already registered! <a href="/register">Try another username</a>'


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username'].strip()
    password = request.form['password'].strip()

    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute(
        'SELECT * FROM users WHERE username = ? AND password = ?',
        (username, password)
    )

    user = c.fetchone()
    conn.close()

    if user:
        session['username'] = username
        return redirect(url_for('home'))

    return 'Invalid username or password! <a href="/login">Try again</a>'


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=5000)
