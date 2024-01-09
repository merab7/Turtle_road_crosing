from turtle import Screen
import time
from turt_car import User_turtle
from cars import Cars
from leve import Board
import sys


def play():
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=700, height=600)
    screen.bgcolor("white")
    screen.tracer(0)
    game_on = True
    level_board = Board()
    player = User_turtle()
    car = Cars()
    screen.listen()
    screen.onkeypress(player.move, "Up")
    while game_on:
        time.sleep(0.1)
        car.move()
        screen.update()
        if car.go_home():
            car.go_home()
        if player.win():
            player.win()
            level_board.add()
            car.speed += 3
        if car.crush(player):
            level_board.game_over()

            def again():
                offer = screen.textinput("Play again", "Type Y to play again or press cancel")
                if offer == "y":
                    screen.clear()
                    return play()
                else:
                    sys.exit()

            again()

    screen.exitonclick()


play()
