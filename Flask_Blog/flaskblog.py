from flask import Flask, render_template, url_for

app = Flask(__name__)    # app is a WSGI application (Web Server Gateway Interface)
                         # __name__ is a name of the application’s module or package.


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
        "contact": 9398809883
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)



