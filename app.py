from flask import request, Flask, render_template, redirect, url_for, flash, session, jsonify
from flask_session import Session
import sqlite3 as sql
from os import urandom


app = Flask(__name__)
app.secret_key = urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/verify", methods=["POST"])
def verify():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin": #change the password checking to use a database
            session["username"] = username
            return redirect(url_for("admin"))
        else:
            flash("Invalid username or password")
            return redirect(url_for("login"))
    else:
        return redirect(url_for("index"))

@app.route("/admin")
def admin():
    if "username" in session:
        return render_template("logged-in.html")
    else:
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))





if __name__ == "__main__":
    app.run(debug=True)