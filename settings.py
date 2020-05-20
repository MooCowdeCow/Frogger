#Based on Chris Bradfield's "Tile-based game Part 1: Setting up"
#https://www.youtube.com/watch?v=3UxnelT9aCo&list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i

#Module imports
import pygame as pg
from os import path

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (40, 40, 40)
LIGHT_GREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#Resolution settings
WIDTH = 990
HEIGHT = 768
FPS = 60
TITLE = "Frogger"
BG_COLOR = DARK_GREY
game_dir = path.join(path.dirname(__file__))

TILESIZE = 33
GRID_WIDTH = WIDTH / TILESIZE
GRID_HEIGHT = HEIGHT / TILESIZE

#Player settings
player_image = pg.image.load(game_dir + "/img/Frogger.png")

#Mob setting
mob_image = pg.image.load(game_dir + "/img/car.png")

#Background settings
# background_image = pg.image.load(game_dir + "/img/bg.png")
# background_rect = background_image.get_rect()