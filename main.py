from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_from_wall()

    # Detect collision from paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() >= 330) or (ball.distance(l_paddle) < 50 and ball.xcor() <= -330):
        ball.bounce_from_paddle()

    # Detect if right paddle missed the ball
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increment_left_score()

    # Detect if left paddle missed the ball
    elif ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increment_right_score()

screen.exitonclick()

