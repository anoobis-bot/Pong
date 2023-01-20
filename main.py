import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
from drawer import FieldDrawer

# Window properties
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"

REFRESH_RATE = 0.05


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

    field_drawer = FieldDrawer(SCREEN_HEIGHT)

    while True:
        player_2.move_bot()
        ball.move_forward()

        if ball.on_wall(SCREEN_HEIGHT):
            ball.bounce_wall()
        elif ball.on_player(player=player_1, screen_width=SCREEN_WIDTH):
            ball.bounce_player()
        elif ball.on_player(player=player_2, screen_width=SCREEN_WIDTH):
            ball.bounce_player()

        if ball.xcor() > SCREEN_WIDTH / 2:
            ball.start_position()
            player_1.increment_score()
            scoreboard_1.display_score()
        elif ball.xcor() < -(SCREEN_WIDTH / 2):
            ball.start_position()
            player_2.increment_score()
            scoreboard_2.display_score()

        screen.update()
        time.sleep(REFRESH_RATE)


    screen.mainloop()


main()
