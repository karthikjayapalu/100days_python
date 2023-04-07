from turtle import Turtle


# TODO: 2. Create and move a paddle
# width =20
# height=100
# x_pos=350
# y_pos=0
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def w(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def s(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)