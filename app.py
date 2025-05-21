#!/usr/bin/python3
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html", title="Maddy's Braggalicious Bragging Board")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    if not name or not email:
        return render_template("home.html", title="Maddy's Braggalicious Bragging Board", error="Please fill in all fields.")
    
    conn = sqlite3.connect('db.sql')
    c = conn.cursor()
    c.execute("insert into users (name, email, message) values (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()
    return render_template("home.html", title="Maddy's Braggalicious Bragging Board", success="Message submitted successfully!")    

application = app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
