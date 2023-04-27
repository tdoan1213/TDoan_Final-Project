# File by Tim Doan

# libraries
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

# left player class

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game 
        self.image = pg.Surface((25,75))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.confric = 0.1

    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC

    def inbounds(self):
        if self.rect.x > WIDTH:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
            print("i am off the right side of the screen...")
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
            print("i am off the left side of the screen...")
        if self.rect.y > HEIGHT:
            print("i am off the bottom of the screen")
        if self.rect.y < 0:
            print("i am off the top of the screen...")

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

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