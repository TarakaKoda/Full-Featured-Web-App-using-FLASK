from flask import render_template, url_for, flash, redirect
from __init__ import app
from forms import RegistrationForm, LoginForm
from models import User, Post

posts = [
    {
        "author": "Srinivasu Koda",
        "title": "Blog Post 1",
        "content": "This is my first post",
        "date": "June 30, 2023",
        "contact": 906910000
    },
    {
        "author": "Naga Pavan",
        "title": "Blog Post 2",
        "content": "This is my second post",
        "date": "July 23, 2023",
        "contact": 9398809893
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome to Thunder ⚡  {form.username.data}!  We're thrilled to have you join us!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "nagapavan@gmail.com" and form.password.data == "password":
            flash(f" I just sensed the weather is changing. Maybe the God Of Thunder ⚡ has arrived! Enjoy your stay.", "success")
            return redirect(url_for("home"))
        else:
            flash(f"⚠ Thunder Strikes! Login Unsuccessful. Please check Email and Password", "danger")
    return render_template("login.html", tilte="Login", form=form)
