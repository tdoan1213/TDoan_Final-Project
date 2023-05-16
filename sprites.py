import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint


vec = pg.math.Vector2

# player classes
class Player(Sprite):
    def __init__(self, game, p1p2, x, y, color):
        Sprite.__init__(self)
        # these are the properties
        self.game = game
        self.image = pg.Surface((25,150))
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/4, HEIGHT/2)
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.p1p2 = p1p2

    def inputA(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.vel.y = -10
        if keystate[pg.K_s]:
            self.vel.y = 10

    def inputB(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_i]:
            self.vel.y = -10
        if keystate[pg.K_k]:
            self.vel.y = 10 

    def update(self):
        # self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = 0
        if self.p1p2 == 1:
            self.inputB()
        else:
            self.inputA()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Ball(Sprite):
    def __init__(self,x,y,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (WIDTH/4, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(7)
        self.acc = vec(1,1)
        self.cofric = 0.01

    def inbounds(self):
        if self.rect.x > WIDTH - 75:
            self.vel.x *= -1
            self.acc = self.vel * -self.cofric
            self.pos = (WIDTH/2, HEIGHT/2)
        if self.rect.x < 25:
            self.vel.x *= -1
            self.pos = (WIDTH/2, HEIGHT/2)
            self.acc = self.vel * -self.cofric
        if self.rect.y < 25:
            self.vel.y *= -1
            self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT - 75:
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
        