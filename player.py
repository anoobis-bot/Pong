from turtle import Turtle

PLAYER_COLOR = "white"
TURTLE_SIZE = 20
PLAYER_SIZE = 3.5
PLAYER_SIZE_PADDING = (TURTLE_SIZE / 2) * 3

MOVE_DIST = 15


class Player(Turtle):
    def __init__(self, player_id, screen):
        super().__init__()
        self.shape("square")
        self.color(PLAYER_COLOR)
        self.penup()
        self.shapesize(stretch_wid=PLAYER_SIZE, stretch_len=0.5)

        self.player_id = player_id
        self.init_location(screen.window_width())
        self.screen_height = screen.window_height()

        self.is_bot = -1
        self.bot_direction = 'u'

        self.score = 0

    def init_location(self, screen_width):
        if self.player_id == 1:
            self.goto(x=-(screen_width / 2) + (PLAYER_SIZE_PADDING * 2), y=0)
        elif self.player_id == 2 or self.player_id == -1:
            self.goto(x=(screen_width / 2) - (PLAYER_SIZE_PADDING * 2), y=0)

    def move_up(self):
        if self.ycor() < (self.screen_height / 2) - ((TURTLE_SIZE * PLAYER_SIZE) / 2):
            self.sety(self.ycor() + MOVE_DIST)

    def move_down(self):
        if self.ycor() > -(self.screen_height / 2) + ((TURTLE_SIZE * PLAYER_SIZE) / 2):
            self.sety(self.ycor() - MOVE_DIST)

    def set_bot(self):
        self.is_bot = 1
        self.bot_direction = 'u'

    def move_bot(self):
        if self.is_bot == -1:
            return

        if self.bot_direction == 'u':
            if self.ycor() < (self.screen_height / 2) - ((TURTLE_SIZE * PLAYER_SIZE) / 2):
                self.sety(self.ycor() + MOVE_DIST)
            else:
                self.bot_direction = 'd'

        elif self.bot_direction == 'd':
            if self.ycor() > -(self.screen_height / 2) + ((TURTLE_SIZE * PLAYER_SIZE) / 2):
                self.sety(self.ycor() - MOVE_DIST)
            else:
                self.bot_direction = 'u'

    def increment_score(self):
        self.score += 1
