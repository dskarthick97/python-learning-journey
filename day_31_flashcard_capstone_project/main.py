""" Flashcard Capstone App """

import tkinter
from random import choice

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_data = {}
dict_data = {}

# read the data's from the csv
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    dict_data = original_data.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")


def next_card():
    global random_data, flip_timer
    window.after_cancel(flip_timer)
    random_data = choice(dict_data)
    
    canvas.itemconfig(lan, text="French", fill="black")
    canvas.itemconfig(translate, text=random_data.get("French"), fill="black")
    canvas.itemconfig(card_bg, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(lan, text="English", fill="white")
    canvas.itemconfig(translate, text=random_data.get("English"), fill="white")
    canvas.itemconfig(card_bg, image=card_back_image)


def is_known():
    dict_data.remove(random_data)
    data = pd.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = tkinter.Canvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0
)
card_front_image = tkinter.PhotoImage(file="./images/card_front.png")
card_back_image = tkinter.PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_image)
lan = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
translate = canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(
    image=wrong_image, highlightthickness=0, command=next_card
)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(
    image=right_image, highlightthickness=0, command=is_known
)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
