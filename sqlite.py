from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect("database.db")
    # Check if the table already exists
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
    table_exists = cursor.fetchone() is not None
    if not table_exists:
        # If the table doesn't exist, create it
        conn.execute('CREATE TABLE students (name TEXT)')
        conn.commit()
    conn.close()
    return render_template('content.html', msg="DB is ready")

@app.route('/insert')
def create_record():
    name= "Mzy"
    with sqlite3.connect("database.db") as conn:
        cur  = conn.cursor()
        cur.execute("insert into students (name) values (?)", [name])
        conn.commit()
    return render_template('content.html', msg= "name has been inserted")

@app.route('/dynamic/<text>')
def dynamic_route(text):
    with sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name) VALUES (?)", [text])
        conn.commit()
    return render_template('content.html', msg=f"{text} has been inserted")


@app.route('/select')
def select_records():
    with sqlite3.connect("database.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        names = cur.fetchall()

    return render_template('content.html', names_content=names)


app.run()
 