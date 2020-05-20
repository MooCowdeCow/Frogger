#Based on Chris Bradfield's "Tile-based game Part 1: Setting up"
#https://www.youtube.com/watch?v=3UxnelT9aCo&list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i

#Module imports
import pygame as pg
from random import *
from settings import *

#Player Sprite
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # self.image = player_image
        self.image = pg.transform.scale(player_image, (TILESIZE,TILESIZE))
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        #Player wall collision
        if not self.collide_with_walls(dx, dy): 
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    #Screen border Sprite
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * 31.9
        self.rect.y = y * 32

class Mob(pg.sprite.Sprite):
    #Mob Sprite
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.transform.scale(mob_image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speedx = 8
        self.speedy = 0

    def move(self, dx=0, dy=0):
        #Mob collision
        if not self.collide_with_walls(dx, dy): 
            self.x = x
            self.y = y

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH:
        #or self.rect.x <=0 + TILESIZE
            self.rect.x = 0
            self.rect.y += TILESIZE*randint(1,5)