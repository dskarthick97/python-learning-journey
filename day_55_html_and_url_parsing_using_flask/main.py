"""
Hello world function with flask.
"""

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    """A decorator function for making a text bold."""

    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    """A decorator function for making a text italics."""

    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underlined(function):
    """A decorator function for making a text underlined."""

    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'


# different routes using the app.route decorator
@app.route("/bye")
@make_underlined
@make_emphasis
@make_bold
def say_bye():
    return "Bye!"


# creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello, {name}!. You're {age} old"


def main():
    app.run(
        debug=True
    )  # debug mode will automatically detects the changes in the code and reloads the server.


if __name__ == "__main__":
    main()
