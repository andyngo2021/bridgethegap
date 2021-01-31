from flask import render_template, url_for, redirect, request
from bridgethegap import app

# Home directory
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/game")
def game():
    return render_template('game.html')


# TEMPORARY SO I CAN FIGURE OUT THE LAYOUT.HTML THAT OTHER PAGES CAN INHERIT FROM
@app.route("/layout")
def layout():
    return render_template('layout.html')