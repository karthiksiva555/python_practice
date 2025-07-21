from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# draw a dashed line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# draw different shapes
colors = ['red', 'royal blue', 'green', 'yellow', 'black']
for sides in range(3, 11):
    degrees = 360/sides
    colour = random.choice(colors)
    timmy.color(colour)

    for _ in range(sides):
        timmy.forward(50)
        timmy.right(degrees)

screen = Screen()
screen.exitonclick()

# 3 ways of importing
# 1. import <package> and then <package>.class_name
import random
num = random.randint(1, 10)

# 2. from <package> import class_name
from math import isnan
is_num = isnan("10")

# 3. from <package> import *
# not recommended as it is going to import everything in the package

# use alias for long names: import <long_package_name> as <short_code>
# import tkinter as tk

# use pip install <package_name> to install external packages


