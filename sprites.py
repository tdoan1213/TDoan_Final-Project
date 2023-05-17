# File created by: Tim Doan

# imported libraries 
import pygame as pg
from time import sleep
from pygame.sprite import Sprite
from settings import *
from random import randint


vec = pg.math.Vector2

# player class
class Player(Sprite):
    def __init__(self, game, p1p2, x, y, color):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((20,100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/4, HEIGHT/2)
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.p1p2 = p1p2
# keybinds for left player 
    def inputA(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.vel.y = -10
        if keystate[pg.K_s]:
            self.vel.y = 10
# keybinds for right player
    def inputB(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_i]:
            self.vel.y = -10
        if keystate[pg.K_k]:
            self.vel.y = 10 
# differentiates the player binds
    def update(self):
        self.acc.x = 0
        if self.p1p2 == 1:
            self.inputB()
        else:
            self.inputA()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
# ball class
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
# bounds for ball
    def inbounds(self):
        if self.rect.x > WIDTH - 75:
            self.vel.x *= -1
            self.acc = self.vel * -self.cofric
            sleep(3)
            self.pos = (WIDTH/2, HEIGHT/2)
        if self.rect.x < 25:
            self.vel.x *= -1
            sleep(3)
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
        self.pos += self.vel
        self.rect.center = self.pos
# wall class
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
# roof class
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
        