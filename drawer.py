from turtle import Turtle

LINE_DIST = 15
LINE_WIDTH = 5

STADIUM_COLOR = "white"

SOUTH = 270


class FieldDrawer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color()

    def draw_stadium_lines(self, screen_height):
        self.goto(x=0, y=screen_height / 2)
        self.setheading(SOUTH)
        self.color(STADIUM_COLOR)
        self.width(LINE_WIDTH)
        while self.ycor() > -(screen_height / 2):
            self.pendown()
            self.forward(LINE_DIST)
            self.penup()
            self.forward(LINE_DIST)
