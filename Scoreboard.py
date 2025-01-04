from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.current_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f" {self.current_score} ", False, "center", ("Courier", 55, "bold"))

    def update_score(self):
        self.current_score+=1
        self.clear()
        self.update_scoreboard()

    def end_game(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", ("Courier", 24, "normal"))