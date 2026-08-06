from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'nci-library-secret-key'

# Creating the user database table
def init_db():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT NOT NULL UNIQUE, 
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

# Home page routing
@app.route('/')
def home():
    return 'Welcome to NCI Library System! Go to <a href="/register">Register</a> or <a href="/login">Login</a>.'

# Showing Register page (GET)
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

# Saving Register data to database (POST)
@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    
    return redirect(url_for('login'))

# Showing Login page (GET)
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

    # Validating Login data 
@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    # Checking if user and password exists in the databse 
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    
    if user:
        return f"<h1>Welcome back, {username}!</h1><p>Login successful.</p><br><a href='/login'>Logout</a>"
    else:
        return "Invalid username or password! <a href='/login'>Try again</a>"

if __name__ == '__main__':
    app.run(port=5000)
