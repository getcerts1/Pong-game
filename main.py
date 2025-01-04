import turtle as t
from RPad import Pad
import time
from ball import Ball
from ground import Ground
from Scoreboard import Scoreboard

# Set up the screen
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

START_POSITION_R = (350,0)
START_POSITION_L = (-350, 0)
player_1 = 0
player_2 = 0

r_pad = Pad(START_POSITION_R)
l_pad = Pad(START_POSITION_L)
ball = Ball()
ground = Ground()
scoreboard_l = Scoreboard((300,220))
scoreboard_r = Scoreboard((-300,220))

screen.listen()
screen.onkey(r_pad.move_up, "Up")
screen.onkey(r_pad.move_down, "Down")
screen.onkey(l_pad.move_up, "w".lower())
screen.onkey(l_pad.move_down, "s".lower())

x,y = l_pad.position()
print((x,y))
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)


    ball.move()


    # if x.cor goes beyond pad, +1 point

    if ball.xcor() > 380:  # Horizontal boundaries
        ball.setheading(180 - ball.heading())
        player_1+=1
        print(f'player1: {player_1}')
        scoreboard_r.update_score()
        scoreboard_r.update_scoreboard()
        ball.reset()
    elif ball.xcor() < -380:
        ball.setheading(180 - ball.heading())
        player_2+=1
        print(f'player2: {player_2}')
        scoreboard_l.update_score()
        scoreboard_l.update_scoreboard()
        ball.reset()

    if ball.ycor() > 300 or ball.ycor() < -300:  # Vertical boundaries
        ball.setheading(-ball.heading())  # Reverse vertical direction



    if (350 > ball.xcor() > 340) and (r_pad.ycor() + 100 > ball.ycor() > r_pad.ycor() - 100):
        ball.setheading(180 - ball.heading())
    elif (-340 > ball.xcor() > -350) and (l_pad.ycor() + 100 > ball.ycor() > l_pad.ycor() - 100):
        ball.setheading(180 - ball.heading())

    if scoreboard_r.current_score == 5 or scoreboard_l.current_score == 5:
        scoreboard_r.end_game()
        break



screen.exitonclick()
