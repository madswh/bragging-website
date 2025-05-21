#!/usr/bin/python3
from flask import Flask, render_template, request
from __init__ import database, emailer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html", title="Maddy's Braggalicious Bragging Board")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    database.save_to_db(name, email, message)
    emailer.send_email(email,"Thank you for your message!", f'Your message: \n{message}\n has been received. I will get back to you soon!')
    return render_template("home.html", title="Maddy's Braggalicious Bragging Board", message="Your message has been submitted!")

application = app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
