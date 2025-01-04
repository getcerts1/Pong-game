from turtle import Turtle
import random
UPPER_LIMIT = 280
SET_DIRECTION = random.randint(1,330)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(1)
        self.setheading(SET_DIRECTION)  # Set initial direction at 45 degrees

    def move(self):
        self.forward(10)

        # Check for boundary collision

    def reset(self):
        self.clear()
        self.goto(0,0)
