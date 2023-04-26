import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)  # app is a WSGI application (Web Server Gateway Interface)
# __name__ is a name of the application’s module or package.

app.config["SECRET_KEY"] = "1de386d816c4c0484ffa4e3dc43f21ea"  # this is used for protection from the treats.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = 'warning'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USER_TLS"] = False
app.config["MAIL_USER_SSL"] = True
app.config["MAIL_USERNAME"] = "youremail@gmail.com"
app.config["MAIL_PASSWORD"] = "yourpassword"
mail = Mail(app)

from flaskblog import routes
