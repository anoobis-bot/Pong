from turtle import Turtle

LINE_DIST = 15

STADIUM_COLOR = "white"

SOUTH = 270


class FieldDrawer(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color()

        self.draw_stadium(screen_height)

    def draw_stadium(self, screen_height):
        self.goto(x=0, y=screen_height / 2)
        self.setheading(SOUTH)
        self.color(STADIUM_COLOR)
        while self.ycor() < -(screen_height / 2):
            self.pendown()
            self.forward(LINE_DIST)
            self.penup()
            self.forward(LINE_DIST)
