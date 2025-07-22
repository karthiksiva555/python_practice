import random
import turtle
from turtle import Turtle, Screen
from colorgram import extract

turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")

screen = Screen()
screen.setup(800, 600)

colors = extract('damien_hirst_spot_painting.jpg', 20)

def random_color_from_painting():
    color = random.choice(colors)
    return color.rgb

def start_at_left_bottom():
    left = screen.window_width() // -2
    bottom = screen.window_height() // -2
    timmy.goto(left+50, bottom+50)

def go_to_one_row_above():
    current_y = timmy.position()[1]
    left = screen.window_width() // -2
    timmy.goto(left+50, current_y+50)

def draw_row():
    x, y = timmy.position()
    right_limit = screen.window_width() // 2
    while x < right_limit:
        timmy.dot(20, random_color_from_painting())
        timmy.forward(50)
        x = timmy.position()[0]

def below_upper_range():
    x, y = timmy.position()
    upper_limit = screen.window_height() // 2
    return y < upper_limit

def damien_hirst_painting():
    timmy.penup()
    start_at_left_bottom()
    while below_upper_range():
        draw_row()
        go_to_one_row_above()
    timmy.hideturtle()

damien_hirst_painting()

screen.exitonclick()