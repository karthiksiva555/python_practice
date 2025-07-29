from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# move forward on pressing space key
# def move_forward():
#     timmy.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.exitonclick()

# function taking another function as input
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def calculator(num1, num2, function):
    return function(num1, num2)

result = calculator(10, 5, multiply)
print(result)


# Etch a Sketch exercise
# Press 'W' to move forward, 'S' to move backwards, A > Anti-clockwise, D > clockwise, C > Clear drawing

def move_forward():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_counter_clockwise():
    timmy.left(10)

def turn_clockwise():
    timmy.right(10)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()




