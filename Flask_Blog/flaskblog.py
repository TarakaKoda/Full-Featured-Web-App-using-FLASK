from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)    # app is a WSGI application (Web Server Gateway Interface)
                         # __name__ is a name of the application’s module or package.

app.config["SECRET_KEY"] = "1de386d816c4c0484ffa4e3dc43f21ea"  # this is used for protection from the treats.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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


if __name__ == "__main__":
    app.run(debug=True)



