
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# T1: Creating the user database table
def init_db():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT NOT NULL, 
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Running database setup
init_db()

# Home page routing
@app.route('/')
def home():
    return 'Welcome to NCI Library System! Go to <a href="/register">Register</a> or <a href="/login">Login</a>.'

# Routing to show the Register page
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

# Routing to show the Login page
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=5000)
