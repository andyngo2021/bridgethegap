from flask import render_template, url_for, redirect, request
from bridgethegap import app

# Home directory
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/page_2")
def page_2():
    return render_template('Page-2.html')