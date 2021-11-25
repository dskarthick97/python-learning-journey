"""
Simple personal site using flask.
"""

from flask import Flask
from flask import render_template, url_for


app = Flask(__name__)
# url_for("static", filename="style.css")


@app.route("/")
def home():
    return render_template("index.html")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
