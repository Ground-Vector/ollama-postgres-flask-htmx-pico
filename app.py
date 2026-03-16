from flask import Flask, render_template, request

from database import get_users, add_user
from library import database_handle
from utils import build_page

app = Flask(__name__)
db = database_handle()


@app.route("/")
def index():
    return render_template("index.html", **build_page(db))


@app.route("/register", methods=["GET", "POST"])
def register():
    errors = []
    if request.method == "POST":
        name = request.form.get("name")
        if len(name) > 0:
            add_user(db, name)
        else:
            errors.append("Name is required")
    return render_template("register.html", **build_page(db), errors=errors, users=get_users(db))
