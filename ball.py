from turtle import Turtle
import random

random.seed()

BALL_SPEED = 13

NORTH = 90
SOUTH = 270
EAST = 0
EAST_360 = 360
WEST = 180
ANGLE_MARGIN = 20

TURTLE_SIZE = 20
STRETCH_FACTOR = 0.8


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=-STRETCH_FACTOR, stretch_len=STRETCH_FACTOR)
        self.start_position()

    def start_position(self):
        self.home()
        r = random.choice([(EAST, NORTH - ANGLE_MARGIN), (NORTH + ANGLE_MARGIN, WEST - 1),
                           (WEST, SOUTH - ANGLE_MARGIN), (SOUTH + ANGLE_MARGIN, EAST_360)])
        self.setheading(random.randint(*r))

    def move_forward(self):
        self.forward(BALL_SPEED)

    def on_wall(self, screen_height):
        if abs(self.ycor()) > screen_height / 2 - (TURTLE_SIZE * STRETCH_FACTOR):
            return True
        else:
            return False

    def on_player(self, player, screen_width):
        if player.player_id == 1:
            if self.xcor() <= -(screen_width / 2) + player.padding_size + ((TURTLE_SIZE * player.stretch_length)) \
                    and (player.ycor() - (TURTLE_SIZE * player.string_height) / 2) <= self.ycor() <= \
                        (player.ycor() + (TURTLE_SIZE * player.string_height) / 2):
                return True

        elif player.player_id == 2 or player.player_id == -1:
            if self.xcor() >= (screen_width / 2) - player.padding_size - ((TURTLE_SIZE * player.stretch_length)) \
                    and (player.ycor() - (TURTLE_SIZE * player.string_height) / 2) <= self.ycor() <= \
                        (player.ycor() + (TURTLE_SIZE * player.string_height) / 2):
                return True

        return False

    def bounce_wall(self):
        if EAST < self.heading() < NORTH:
            self.setheading(EAST_360 - self.heading())
        elif NORTH < self.heading() < WEST:
            self.setheading(WEST + (WEST - self.heading()))
        elif WEST < self.heading() < SOUTH:
            self.setheading(WEST - (self.heading() - WEST))
        elif SOUTH < self.heading() < EAST_360:
            self.setheading(EAST_360 - self.heading())

        else:
            self.setheading((self.heading() + 180) % 360)

    def bounce_player(self):
        if EAST < self.heading() < NORTH:
            self.setheading(WEST - self.heading())
        elif NORTH < self.heading() < WEST:
            self.setheading(WEST - self.heading())
        elif WEST < self.heading() < SOUTH:
            self.setheading(EAST_360 - (self.heading() - WEST))
        elif SOUTH < self.heading() < EAST_360:
            self.setheading(EAST_360 - self.heading())

        else:
            self.setheading((self.heading() + 180) % 360)
