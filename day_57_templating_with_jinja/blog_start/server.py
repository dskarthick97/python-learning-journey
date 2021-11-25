"""
Rendering blog cards using Jinja templates.
"""

import requests

from flask import Flask, render_template

from post import Post


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to the blog..</h1>"


@app.route("/blogs")
def render_blogs():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", blog_posts=response)


@app.route("/blogs/<int:blog_id>")
def get_blog(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()[
        blog_id - 1
    ]
    post = Post(response["title"], response["subtitle"], response["body"])
    return render_template("post.html", post=post)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
