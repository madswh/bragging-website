#!/usr/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

app.run("0.0.0.0", 5000, debug=True)