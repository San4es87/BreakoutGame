from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import ScoreBoard
import time


index_list = [-450, -400, -350, -300, -250, -200, -150, -100, - 50, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
index_list1 = [50, 20, -10, -30, - 60]
color = ["red", "orange", "blue", "yellow", "green"]
all_bricks = []

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()






for count_tur in range(0, 19):
    bricks = Bricks((index_list[count_tur], 100))
    bricks.color('red')
    all_bricks.append(bricks)
for count_tur in range(0, 19):
    bricks = Bricks((index_list[count_tur], 70))
    bricks.color('orange')
    all_bricks.append(bricks)
for count_tur in range(0, 19):
    bricks = Bricks((index_list[count_tur], 40))
    bricks.color('blue')
    all_bricks.append(bricks)
for count_tur in range(0, 19):
    bricks = Bricks((index_list[count_tur], 10))
    bricks.color('yellow')
    all_bricks.append(bricks)
for count_tur in range(0, 19):
    bricks = Bricks((index_list[count_tur], -20))
    bricks.color('green')
    all_bricks.append(bricks)

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=paddle.go_left, key="Left")
screen.onkey(fun=paddle.go_right, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()



    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.ycor() < -280:
        ball.rest()
        scoreboard.minus_score()
        scoreboard.upload_score()

    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_y()



    for brick in all_bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            scoreboard.plus_score()
            scoreboard.upload_score()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.bounce_x()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                # ball.bounce_x()
                ball.bounce_y()
            all_bricks.remove(brick)





screen.exitonclick()