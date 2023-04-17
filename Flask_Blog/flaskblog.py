from flask import Flask

app = Flask(__name__)  # app is an instance of WSGI (Web Server Gateway Interface)
                       # __name__ is a name of the application’s module or package (eg. flaskblog)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


