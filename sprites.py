import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint


vec = pg.math.Vector2

# left player class
class PlayerL(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((25,150))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/4, HEIGHT/2)
        self.pos = vec(WIDTH/8, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False

# right player class
class PlayerR(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((25,150))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/4, HEIGHT/2)
        self.pos = vec(WIDTH*7/8, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False

    def input(self, PlayerR):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_i]:
            self.vel.y = -10
        if keystate[pg.K_k]:
            self.vel.y = 10
    def input(self, PlayerL):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.vel.y = -10
        if keystate[pg.K_s]:
            self.vel.y = 10 

    # def input(PlayerR, self):
    #     keystate = pg.key.get_pressed()
    #     if keystate[pg.K_i]:
    #         self.vel.y = -4
    #     if keystate[pg.K_k]:
    #         self.vel.y = 4

    def update(self):
        # self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = 0
        self.input(PlayerR)
        self.input(PlayerL)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/4, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            self.vel.x *= -1
            self.acc = self.vel * -self.cofric
        if self.rect.x < 0:
            self.vel.x *= -1
            self.acc = self.vel * -self.cofric
        if self.rect.y < 0:
            self.vel.y *= -1
            self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT:
            self.vel.y *= -1
            self.acc = self.vel * -self.cofric
    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos

class Wall(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant

class Roof(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant
        