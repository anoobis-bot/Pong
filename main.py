import time
from turtle import Screen
from player import Player

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
    screen.onkeypress(key="w", fun=player_1.move_up)
    screen.onkeypress(key="s", fun=player_1.move_down)

    player_2.set_bot()

    while True:
        player_2.move_bot()
        screen.update()
        time.sleep(REFRESH_RATE)


    screen.mainloop()


main()
