from turtle import Turtle

PLAYER_COLOR = "white"
TURTLE_SIZE = 20
HEIGHT_STRETCH = 3.5
WIDTH_STRETCH = 0.5
PLAYER_SIZE_PADDING = (TURTLE_SIZE / 2) * 3

MOVE_DIST = 15
"""Distance in pixels on how fast the player paddles are moving per refresh"""
BOT_MOVE_DIST = 5


class Player(Turtle):
    def __init__(self, player_id, screen):
        super().__init__()
        self.shape("square")
        self.color(PLAYER_COLOR)
        self.penup()
        # read shapesize() docs for the naming convention
        self.shapesize(stretch_wid=HEIGHT_STRETCH, stretch_len=WIDTH_STRETCH)
        # Padding of the paddle so that they are not at the window's edge
        # See init_location() to see how the paddles are placed into the GUI
        self.padding_size = (TURTLE_SIZE * WIDTH_STRETCH * 3) * 2

        # For the player id system, there could only be 3 possible numbers. -1, 1, 2
        # -1 denotes that the player is a bot
        # 1 and 2 denotes players 1 and 2 respectively.
        # as of January 20, 2023, player 2's implementation is still not finished.
        self.player_id = player_id
        self.init_location(screen.window_width())
        self.screen_height = screen.window_height()

        # Initial direction that the bot will take.
        # See move_bot() method to know how the bot moves
        self.bot_direction = 'u'

        # TODO explain can hit functionality
        self.can_hit = True

        self.score = 0

    def init_location(self, screen_width):
        if self.player_id == 1:
            self.goto(x=-(screen_width / 2) + (PLAYER_SIZE_PADDING * 2), y=0)
        elif self.player_id == 2 or self.player_id == -1:
            self.goto(x=(screen_width / 2) - (PLAYER_SIZE_PADDING * 2), y=0)

    def move_up(self):
        if self.ycor() < (self.screen_height / 2) - ((TURTLE_SIZE * HEIGHT_STRETCH) / 2):
            self.sety(self.ycor() + MOVE_DIST)

    def move_down(self):
        if self.ycor() > -(self.screen_height / 2) + ((TURTLE_SIZE * HEIGHT_STRETCH) / 2):
            self.sety(self.ycor() - MOVE_DIST)

    def move_bot(self, ball):
        # Since the bot's movement is not dependent on the user's input, it has its' own instructions on how it moves
        if self.player_id != -1:
            return

        # TODO explain bot AI
        if ball.ycor() > self.ycor() + MOVE_DIST / 2:
            if self.ycor() < (self.screen_height / 2) - ((TURTLE_SIZE * HEIGHT_STRETCH) / 2):
                self.sety(self.ycor() + BOT_MOVE_DIST)
            else:
                self.bot_direction = 'd'

        elif ball.ycor() < self.ycor() - MOVE_DIST / 2:
            if self.ycor() > -(self.screen_height / 2) + ((TURTLE_SIZE * HEIGHT_STRETCH) / 2):
                self.sety(self.ycor() - BOT_MOVE_DIST)
            else:
                self.bot_direction = 'u'

    def is_hit(self, ball):
        if not self.can_hit:
            return False

        half_width_len = ((TURTLE_SIZE * WIDTH_STRETCH) / 2)
        half_height_len = ((TURTLE_SIZE * HEIGHT_STRETCH) / 2)
        if self.xcor() - half_width_len <= ball.xcor() <= self.xcor() + half_width_len:

            if self.ycor() - half_height_len <= ball.ycor() <= self.ycor() + half_height_len:
                return True

        return False

    def increment_score(self):
        self.score += 1
