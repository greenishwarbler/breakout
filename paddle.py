from turtle import Turtle

MOVE_PADDLE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=0.5, stretch_len=2)

    def go_left(self):
        if self.xcor() > -282.5:
            new_x = self.xcor() - MOVE_PADDLE
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 282.5:
            new_x = self.xcor() + MOVE_PADDLE
            self.goto(new_x, self.ycor())

    def shrink_paddle(self):
        self.shapesize(stretch_wid=0.5, stretch_len=1)


