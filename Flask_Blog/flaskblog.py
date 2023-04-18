from flask import Flask

app = Flask(__name__)    # app is a WSGI application (Web Server Gateway Interface)
                         # __name__ is a name of the application’s module or package.


@app.route("/")
@app.route("/home")
def home_page():
    return f"<h1>Home Page</h1>" \
           f"<h1>Welcome to our home page</h1>"


@app.route("/about")
def about_page():
    return f"<h1>This is our about page</h1>"


@app.route("/login")
def login_page():
    return f"<h1>This is our Login Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)

