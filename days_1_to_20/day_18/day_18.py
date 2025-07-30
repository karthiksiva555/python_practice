import turtle
from turtle import Turtle, Screen

# 3 ways of importing
# 1. import <package> and then <package>.class_name
import random
num = random.randint(1, 10)

# 2. from <package> import class_name
from math import isnan
not_num = 10
is_num = isnan(not_num)

# 3. from <package> import *
# not recommended as it is going to import everything in the package

# use alias for long names: import <long_package_name> as <short_code>
# import tkinter as tk

# use pip install <package_name> to install external packages

# Turtle challenges
turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = Screen()
screen.setup(800, 600)

def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

# draw a dashed line
def draw_dashed_line():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

# draw different shapes
def draw_different_shapes():
    colors = ['red', 'royal blue', 'green', 'yellow', 'black']
    for sides in range(3, 11):
        degrees = 360/sides
        colour = random.choice(colors)
        timmy.color(colour)

        for _ in range(sides):
            timmy.forward(50)
            timmy.right(degrees)

def random_colour():
    """ Explains the usage of Tuple
    returns a random RGB colour each time called"""
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    return r, g, b

# random walk
def start_random_walk():
    # colors = ['red', 'royal blue', 'green', 'gold', 'black', 'light cyan', 'deep sky blue', 'green yellow']
    degrees = [0, 90, 180, 270]
    timmy.pensize(10)
    timmy.speed(10)

    for _ in range(100):
        # timmy.color(random.choice(colors))
        timmy.color(random_colour())
        timmy.forward(20)
        # timmy.right(random.choice(degrees))
        timmy.setheading(random.choice(degrees))

# draw Spirograph
def draw_spirograph():
    timmy.speed("fastest")
    for _ in range(100):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+10)

draw_spirograph()

screen.exitonclick()

