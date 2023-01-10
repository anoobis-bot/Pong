from turtle import Turtle

FONT = "8BIT WONDER"
FONT_SIZE = 40

OFFSET_X = FONT_SIZE * 3
OFFSET_Y = 260 - FONT_SIZE


class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

        self.player = player
        self.init_location()

        self.display_score()

    def init_location(self):
        if self.player.player_id == 1:
            self.goto(x=-OFFSET_X, y=OFFSET_Y)
        elif self.player.player_id == 2 or self.player.player_id == -1:
            self.goto(x=OFFSET_X, y=OFFSET_Y)

    def display_score(self):
        self.clear()
        self.write(arg=self.player.score, move=False, align="center",
                   font=(FONT, FONT_SIZE, "normal"))
