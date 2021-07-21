
from random import choice, random
from turtle import Turtle, Screen

zeus = Turtle()
zeus.shape("turtle")
# zeus.width(15)

directions = [0, 90, 180, 360]

# draws shapes
def generate_shape(turtle, sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)


# for sides in range(3, 11):
#     colour = random_colour()
#     zeus.color(colour)
#     generate_shape(zeus, sides)


# generate random colour
def random_colour():
    return (random(), random(), random())

# random walk
# for _ in range(100):
#     colour = random_colour()
#     zeus.color(colour)
#     zeus.forward(30)
#     zeus.setheading(choice(directions))


# draw spirograph
def draw_spirograph(offset):
    for _ in range(int(360/offset)):
        zeus.color(random_colour())
        zeus.circle(50)
        heading = zeus.heading()
        zeus.setheading(heading + 10)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
