import colorgram

colors = colorgram.extract("./hirst_art.jpg", 30)


def extract_color(colors):
    color_list = []
    for color in colors:
        extract_rgb = color.rgb
        rgb = (extract_rgb.r, extract_rgb.g, extract_rgb.b)
        color_list.append(rgb)

    return color_list


# print(extract_color(colors))

color_list = [
    (1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), 
    (150, 83, 39), (216, 86, 63), (156, 6, 24), (165, 162, 30), (158, 62, 102), 
    (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20), (175, 134, 162), 
    (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85), 
    (144, 227, 217), (121, 193, 147), (220, 177, 216), (100, 218, 229), 
    (251, 198, 1), (116, 170, 192)
]

from turtle import Turtle, Screen
from random import choice

SPACES          = 50
DOT_THICKNESS   = 20
OFFSET_DISTANCE = 10

alpha = Turtle("turtle")
alpha.color("green")

# figure out how to create a dot of thickeness
def draw_line(alpha, spaces, dot_thickness):
    for _ in range(10):
        alpha.dot(dot_thickness, )
        alpha.penup()
        alpha.forward(spaces)


x = 0
y = 0
for _ in range(OFFSET_DISTANCE):
    alpha.goto(x, y)
    y += SPACES
    draw_line(alpha, SPACES, DOT_THICKNESS)

screen = Screen()
screen.exitonclick()
