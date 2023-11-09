import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to
# move the turtle north. If you get stuck, check the video walkthrough in Step 3.
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# listen to up kep press
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()


screen.exitonclick()
