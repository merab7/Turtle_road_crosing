from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-300, 270)
        self.pendown()
        self.write(f"Level: {self.score}", move=False, align='center', font=('Arial', 12, 'bold'))
        self.hideturtle()

    def add(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", move=False, align='center', font=('Arial', 12, 'bold'))

    def game_over(self):
        self.penup()
        self.goto(0, 100)
        self.pendown()
        self.color("red")
        self.write(f"Game over.", move=False, align='center', font=('Arial', 12, 'bold'))