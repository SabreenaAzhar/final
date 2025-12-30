from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = "database.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    if request.method == "POST":
        first = request.form["first"]
        last = request.form["last"]
        email = request.form["email"]
        conn.execute("INSERT INTO people (first, last, email) VALUES (?, ?, ?)",
                     (first, last, email))
        conn.commit()
        return redirect(url_for("index"))

    people = conn.execute("SELECT * FROM people").fetchall()
    return render_template("index.html", people=people)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM people WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first TEXT,
        last TEXT,
        email TEXT
    )
    """)
    conn.commit()
    app.run(debug=True)
