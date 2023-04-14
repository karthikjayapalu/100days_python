import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Move the turtle with Keypress
# Create and move the cars
# Detect collision with Car
# Detect when turtle reaches the other side
# Create a scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("GAME OVER")
            scoreboard.game_over()
            game_is_on =False

    # Detect when turtle reaches the other side of the screen
    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
