"""
Hello world function with flask.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return "Bye"


def main():
    app.run()


if __name__ == "__main__":
    main()
