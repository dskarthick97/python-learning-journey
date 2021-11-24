"""
Higher or Lower url game.
"""

from random import randint

from flask import Flask

rand_number = randint(0, 9)
app = Flask(__name__)


@app.route("/")
def home():
    """Home page of the game."""
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Guess' width='250'>"
    )


@app.route("/<int:number>")
def higher_or_lower(number):
    if number == rand_number:
        return (
            "<h1>You found me!</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Correct answer' width='250'>"
        )
    elif number > rand_number:
        return (
            "<h1>Too high, try again!</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='High answer' width='250'>"
        )
    else:
        return (
            "<h1>Too low, try again!</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Low answer' width='250'>"
        )


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
