from turtle import Turtle


class User_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.setpos(0, -270)

    def move(self):
        self.forward(10)

    def win(self):
        if self.ycor() > 280:
            self.goto(0, -270)
            return True
