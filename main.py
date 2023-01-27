import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
from drawer import FieldDrawer

# Window properties
# The Screen class defines the coordinate system as follows: It divides the given size of the screen
# into 2. The negative and the positive. This means that the coordinate of the upper right part of the screen
# (given a width of 600 and height of 1000) is (300, 500) while the lower left would be (-300, -500) and so on...
# You would see often pieces of codes that divides the screen height or width by 2
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"

REFRESH_RATE = 0.008


def main():
    # Window setup
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_COLOR)
    screen.tracer(0)

    player_1 = Player(player_id=1, screen=screen)
    player_2 = Player(player_id=-1, screen=screen)

    screen.listen()
    screen.onkeypress(key="Up", fun=player_1.move_up)
    screen.onkeypress(key="Down", fun=player_1.move_down)

    ball = Ball()

    scoreboard_1 = Scoreboard(player_1)
    scoreboard_2 = Scoreboard(player_2)

    field_drawer = FieldDrawer()
    field_drawer.draw_stadium_lines(SCREEN_HEIGHT)

    # no game over condition
    while True:
        player_2.move_bot(ball)
        ball.move_forward()

        if ball.on_wall(SCREEN_HEIGHT):
            ball.bounce_wall()
        elif player_1.is_hit(ball):
            ball.bounce_player()
            player_1.can_hit = False
            player_2.can_hit = True
        elif player_2.is_hit(ball):
            ball.bounce_player()
            player_1.can_hit = True
            player_2.can_hit = False

        if ball.xcor() > SCREEN_WIDTH / 2:
            ball.random_heading_angle()
            player_1.increment_score()
            scoreboard_1.display_score()
            player_1.can_hit = True
            player_2.can_hit = True
        elif ball.xcor() < -(SCREEN_WIDTH / 2):
            ball.random_heading_angle()
            player_2.increment_score()
            scoreboard_2.display_score()
            player_1.can_hit = True
            player_2.can_hit = True

        screen.update()
        time.sleep(REFRESH_RATE)

    # screen.mainloop()


main()
