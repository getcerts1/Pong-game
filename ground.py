from turtle import Turtle

POSITIONS = []
num = 300

for i in range(30):
   num-=20
   POSITIONS.append(num)
print(POSITIONS)

class Ground:

    def __init__(self):
        self.init()



    def init(self):
        for position in POSITIONS:
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.shapesize(0.5,0.5)
            segment.goto(0,position)




