from app import app
from flask import render_template, request, redirect, session
from app import db
from sqlalchemy.sql import text
import queries

@app.route("/")
def index():
    return render_template("etusivu.html") 

@app.route("/statistics")
def statistics():
    return render_template("statistics.html") 

@app.route("/lisää")
def lisaa():
    return render_template("lisaa_treeni.html") 

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html") 
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if queries.login(password, username):
            session['username'] = username
        else:
            print('väärä salasana')
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            print('salasanat eroavat')
        queries.register(password2, username)
        #koodia joka tallentaa käyttäjän tietokantan
        return redirect("/")

