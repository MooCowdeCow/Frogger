#Based on Chris Bradfield's "Tile-based game Part 1: Setting up"
#https://www.youtube.com/watch?v=3UxnelT9aCo&list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i

#Module imports
import pygame as pg
import sys
from random import *

#File imports
from os import path
from settings import *
from sprites import *

#Game window initialization
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        img_folder = path.join(game_folder, 'img')
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        #Variable intialization
        self.all_sprites = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.walls = pg.sprite.Group()     
        for i in range(0,10):
            mob = Mob(self, randint(1,10), randint(1,7))       
        #Interpretation of the tile map
        for row, tiles in enumerate (self.map_data):
            for col, tile in enumerate (tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'p':
                    self.Player = Player(self, col, row)
        self.player = Player(self, 15, 22)

    def run(self):
        #While loop to keep the game running until player exits the game(clicks the red X)
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        #Player exits the game
        pg.quit()
        sys.exit()

    def update(self):
        #Update sequence for all sprites
        self.all_sprites.update()

    def draw(self):
        #The drawing sequence for all sprites
        self.screen.fill(WHITE)
        # Mob.draw()
        self.all_sprites.draw(self.screen)
        pg.display.flip()


    def events(self):
        #Player clicks the red X
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            #Movement keys
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.player.move(dx=-1)
                if event.key == pg.K_d:
                    self.player.move(dx=1)
                if event.key == pg.K_w:
                    self.player.move(dy=-1)
                if event.key == pg.K_s:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

#Game window opens
g = Game()
g.show_start_screen()

while True:
    g.new()
    g.run()
    g.show_go_screen()