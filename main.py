# File by Tim Doan

'''
Game Overview:

Goals:
create a working Pong-style game and style it with colors (vertical, maybe horizontal?)

Rules
Once a player hits the ball, it bounces back to the other side. If the ball goes behind the player,
then the other player scores a point.

Freedoms
players are free to move up and down, but not side to side.
'''

# libraries
import pygame as pg
import os
from settings import *
from sprites import *

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# game 
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
def new(self):
    # starting a new game 
    self.score = 0

    self.all_sprites = pg.sprite.Group()
    # self.borders = pg.sprite.Group()
    # self.ball = pg.sprite.Group()

    self.player = Player(self)

    self.all_sprites.add(self.player)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    # def draw_text():

    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

g = Game()

while g.running:
    g

pg.quit()

