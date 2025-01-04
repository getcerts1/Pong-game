from turtle import Turtle

MOVEMENT = 20

class Pad(Turtle):
    def __init__(self, START_POSITION):
        super().__init__()
        self.start_position = START_POSITION
        self.create()

    def create(self):
       self.shape("square")
       self.color("white")
       self.penup()
       self.shapesize(stretch_wid= 5, stretch_len=1)
       self.goto(self.start_position)

    def move_up(self):
        new_y = self.ycor() + MOVEMENT
        if self.ycor() < 240:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVEMENT
        if self.ycor() > -240:
            self.goto(self.xcor(), new_y)