from turtle import *
from random import *


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(turtle, size_of_gap, r):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(r)
        tim.setheading(tim.heading() + size_of_gap)


tim = Turtle()
colormode(255)

tim.speed(0)
tim.pensize(2)
draw_spirograph(tim, 5, 100)


my_screen = Screen()
my_screen.exitonclick()