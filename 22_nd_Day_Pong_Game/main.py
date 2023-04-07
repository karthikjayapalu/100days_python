'''
# TODO: PONG Game

# By Karthig

# TODO: 1. Create Screen
# TODO: 2. Create slider plates
# TODO: 3. Create Ball
# TODO: 4. Create midfield line (split screen equally)
# TODO: 5. Create Scoreboard
# TODO: 6. Create Screen
# TODO: 7. Bounce Ball around the screen

# From Angela
# TODO: 1. Create the screen
# TODO: 2. Create and move a paddle
# TODO: 3. Create another Paddle
# TODO: 4. Create the ball and make it move
# TODO: 5. Detect Collision with wall and bounce
# TODO: 6. Detect Collision with paddle
# TODO: 7. Detect when paddle misses
# TODO: 8. Keep Score

'''
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# TODO: 1. Create the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

b = Ball()

scoreboard=Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    b.move()

    # Detect collision with wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()
    # Detect collision with right paddle
    if b.distance(r_paddle) < 50 and b.xcor() > 320 or b.distance(l_paddle) < 50 and b.xcor() >-320:
        # print("Made Contact")
        b.bounce_x()

    # Detect when right paddle misses
    if b.xcor() > 380:
        b.reset_position()
        scoreboard.update_scoreboard()

    # Detect when left paddle misses
    # if b.xcor() > - 380:
    #     b.reset_position()

screen.exitonclick()
