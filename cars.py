import turtle
from turtle import Turtle
import random

y = random.randint(50, 100)

RANDOM_X_POS = [x for x in range(380, 800, y)]
turtle.colormode(255)
COLORS = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
          (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
          (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
          (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
          (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
          (176, 192, 208), (168, 99, 102)]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.hideturtle()
        self.speed = 5

    def create_car(self):
        for _ in range(30):
            s = Turtle()
            s.penup()
            s.color(random.choice(COLORS))
            s.shape("square")
            s.shapesize(stretch_wid=1, stretch_len=2)
            s.goto(random.randint(340, 1200), random.randint(-230, 230))
            s.setheading(180)
            self.cars.append(s)

    def move(self):
        for x in self.cars:
            x.goto(x.xcor() - self.speed, x.ycor())

    def go_home(self):
        for x in self.cars:
            if x.xcor() < -390:
                x.teleport(random.randint(340, 1200), random.randint(-230, 230))
                return True

    def crush(self, player):
        for x in self.cars:
            if x.distance(player) < 20:
                return True
