from turtle import Turtle, Screen

omega = Turtle(shape="turtle")
omega.color("blue")
screen = Screen()


def move_forward():
    omega.forward(10)


def move_backward():
    omega.backward(10)


def turn_clockwise():
    omega.right(10)


def turn_counter_clockwise():
    omega.left(10)


def clear_screen():
    screen.resetscreen()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_clockwise, key="a")
screen.onkey(fun=turn_counter_clockwise, key="d")
screen.onkey(fun=clear_screen, key="c")


screen.listen()
screen.exitonclick()
