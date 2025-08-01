from turtle import Turtle

TOP_RANGE = 380
BOTTOM_RANGE = -360
STEP = 20
LEFT_PADDLE_POSITIONS = [(-380, 20), (-380, 0), (-380, -20)]
RIGHT_PADDLE_POSITIONS = [(370, 20), (370, 0), (370, -20)]

def get_paddle(positions):
    segments = []
    for position in positions:
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        segments.append(segment)
    return segments

class Paddle:

    def __init__(self, left_or_right):
        if left_or_right == "left":
            self.segments = get_paddle(LEFT_PADDLE_POSITIONS)
        elif left_or_right == "right":
            self.segments = get_paddle(RIGHT_PADDLE_POSITIONS)

    def move_up(self):
        if not self.can_paddle_move_up():
            return

        for segment in self.segments:
            new_position = (segment.xcor(), segment.ycor() + STEP)
            segment.setposition(new_position)

    def move_down(self):
        if not self.can_paddle_move_down():
            return

        for segment in self.segments:
            new_position = (segment.xcor(), segment.ycor() - STEP)
            segment.setposition(new_position)

    def can_paddle_move_up(self):
        head = self.segments[0]
        if head.ycor() < TOP_RANGE:
            return True
        return False

    def can_paddle_move_down(self):
        tail = self.segments[len(self.segments)-1]
        if tail.ycor() > BOTTOM_RANGE:
            return True
        return False

