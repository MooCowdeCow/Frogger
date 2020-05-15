#Based on Chris Bradfield's "Tile-based game Part 1: Setting up"
#https://www.youtube.com/watch?v=3UxnelT9aCo&list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i

#Module imports
import pygame as pg
import sys
#File imports
from os import path
from settings import *
from sprites import *
from camera import *

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
        # img_folder = path.join(game_folder, 'img')
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        # self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()

    def new(self):
        #Variable intialization
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate (self.map_data):
            for col, tile in enumerate (tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile =='p':
                    self.Player = Player(self, col, row)
        self.player = Player(self, 10, 10)
        #Camera to follow the player sprite
        self.camera = Camera(self.map.width, self.map.height)

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
        #Sprite updates
        self.all_sprites.update()
        self.camera.update(self.player)
    # def draw_grid(self):
    #     #The grid dimensions
    #     for x in range(0, WIDTH, TILESIZE):
    #         pg.draw.line(self.screen, LIGHT_GREY, (x, 0), (x, HEIGHT))
    #     for y in range(0, HEIGHT, TILESIZE):
    #         pg.draw.line(self.screen, LIGHT_GREY, (0, y), (WIDTH, y))

    def draw(self):
        #The grid drawing sequence
        self.screen.fill(BG_COLOR)
        # self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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