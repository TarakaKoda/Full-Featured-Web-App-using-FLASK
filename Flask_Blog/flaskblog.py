from flask import Flask
app = Flask(__name__)


@app.route("/")
def home_page():
    return f"<h1>Home Page</h1>" \
           f"<h1>Welcome to our home page</h1>"


@app.route("/about")
def about_page():
    return f"<h1>This is our about page</h1>"


if __name__ == "__main__":
    app.run(debug=True)

