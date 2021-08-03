""" States guessing game """

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the data from the csv
states_data = pd.read_csv("50_states.csv")
states = states_data["state"].tolist()


def create_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    return new_turtle

guessed_states= list()
while len(guessed_states) < 50:
    state = screen.textinput(title=f"{len(guessed_states)}/50 States", 
        prompt="What's another State name?").title()
    
    if state == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        df = pd.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break

    if state in states:
        guessed_states.append(state)
        new_turtle = create_turtle()
        
        state_data = states_data[states_data.state == state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(state)
