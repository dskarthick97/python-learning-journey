""" Turtle race game """

from random import randint
from turtle import Turtle, Screen

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(
    title="Make your bets", 
    prompt="Which turtle will win the race? Enter the color: "
)

x = -230
y = -100
turtles = list()
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 50
    turtles.append(new_turtle)


if user_choice:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print(f"You've won! The {user_choice} turtle wins the race")
            else:
                print(f"You've lost! The {user_choice} turtle lost the race")
            
        distance = randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
