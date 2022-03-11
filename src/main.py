import math
from game_engine import GameEngine
import arcade

SCREEN_TITLE = "Scavenger Game"

SPRITE_IMAGE_SIZE = 128

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_TILES = 0.5

SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

g = GameEngine(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

def run_the_game():
    
    g.setup()
    #g.on_draw()
    # Tell the computer to call the draw command at the specified interval.
    # Original schedule timing: arcade.schedule(update_on_interval, 2.60 / 1000)
    arcade.schedule(update_on_interval, 0.0001 / 1000)
    arcade.run()

def update_on_interval(delta_time):
    g.on_draw()

if __name__ == "__main__":
    run_the_game()
    
   
    