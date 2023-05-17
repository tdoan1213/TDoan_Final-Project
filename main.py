# File created by: Tim Doan

# import libs
from time import sleep
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pong")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.roofs = pg.sprite.Group()

        self.playerL = Player(self, 1, WIDTH - 150, HEIGHT/2, BLACK)
        self.playerR = Player(self, 2, 150, HEIGHT/2, BLACK)
        self.wall1 = Wall(WIDTH, 50, 0, HEIGHT, (255,255,255), "left")
        self.wall2 = Wall(WIDTH, 50, 0, HEIGHT, (255,255,255), "right")
        self.roof1 = Roof(WIDTH, 150, 0, HEIGHT, (255,255,255), "top")
        self.roof2 = Roof(WIDTH, 150, 0, HEIGHT, (255,255,255), "bottom")
        self.ball = Ball(WIDTH/2, HEIGHT/2, 50, 50, WHITE)

        self.all_sprites.add(self.playerL)
        self.all_sprites.add(self.playerR)
        self.all_sprites.add(self.wall1)
        self.all_sprites.add(self.wall2)
        self.all_sprites.add(self.roof1)
        self.all_sprites.add(self.roof2)
        self.all_sprites.add(self.ball)

        self.walls.add(self.wall1)
        self.walls.add(self.wall2)
        self.roofs.add(self.roof1)
        self.roofs.add(self.roof2)
        

        for wall in WALL_LIST:
            w = Wall(*wall)
            self.all_sprites.add(w)
            self.walls.add(w)
        for roof in ROOF_LIST:
            r = Roof(*roof)
            self.all_sprites.add(r)
            self.walls.add(r)

        self.run()
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
        # player bounds
        self.all_sprites.update()
        if self.playerL.pos.y:
            self.playerL.vel.y = 0
        if self.playerL.pos.y:
            self.playerR.vel.y = 0
        if self.playerR.pos.y <= 175:
            hits = pg.sprite.spritecollide(self.playerR, self.roofs, False)
            self.playerR.pos.y = 175
        if self.playerL.pos.y <= 175:
            hits = pg.sprite.spritecollide(self.playerR, self.roofs, False)
            self.playerL.pos.y = 175
        if self.playerR.pos.y >= 725:
            hits = pg.sprite.spritecollide(self.playerR, self.roofs, False)
            self.playerR.pos.y = 725
        if self.playerL.pos.y >= 725:
            hits = pg.sprite.spritecollide(self.playerR, self.roofs, False)
            self.playerL.pos.y = 725
        # ball hitting player bounds
        bhits = pg.sprite.collide_rect(self.ball, self.playerR) or pg.sprite.collide_rect(self.ball, self.playerL)
        if bhits:
            self.ball.vel.x *= -1
    def draw(self):
        self.screen.fill(GRAY)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
        pg.display.update()
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()