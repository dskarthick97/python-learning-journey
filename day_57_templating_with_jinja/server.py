"""
Templating with Jinja using Flask.
"""

from datetime import datetime
from random import randint

import requests

from flask import Flask
from flask import render_template


app = Flask(__name__)


def get(url: str) -> dict:
    return requests.get(url).json()


def get_person_details(name: str) -> dict:
    age = get(f"https://api.agify.io?name={name}")["age"]
    gender = get(f"https://api.genderize.io?name={name}")["gender"]
    return {"name": name, "age": age, "gender": gender}


@app.route("/")
def home():
    return "Welcome to the Matrix.."


@app.route("/guess/<name>")
def person_details(name):
    """Home page url."""
    person_info = get_person_details(name)
    return render_template("index.html", **person_info)


@app.route("/blog")
def blog():
    blog_posts = get("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("blog.html", blog_posts=blog_posts)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
