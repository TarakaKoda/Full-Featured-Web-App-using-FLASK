from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # app is a WSGI application (Web Server Gateway Interface)
# __name__ is a name of the application’s module or package.

app.config["SECRET_KEY"] = "1de386d816c4c0484ffa4e3dc43f21ea"  # this is used for protection from the treats.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from __init__ import routes
