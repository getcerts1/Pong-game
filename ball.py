from turtle import Turtle
import random
UPPER_LIMIT = 280
SET_DIRECTION = random.randint(45,225)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(1)
        self.setheading(30)  # Set initial direction at 45 degrees

    def move(self):
        self.forward(10)

        # Check for boundary collision
        if self.xcor() > 290 or self.xcor() < -290:  # Horizontal boundaries
            self.setheading(180 - self.heading())  # Reverse horizontal direction
        if self.ycor() > 290 or self.ycor() < -290:  # Vertical boundaries
            self.setheading(-self.heading())  # Reverse vertical direction
