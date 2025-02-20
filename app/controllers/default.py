from app import app
from app.auth import load_user
from app.models.user import User
from flask import render_template, redirect, request
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect("/dashboard")    
    return redirect("/login")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user(User.new())
        return redirect("/dashboard")
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
