# File created by: Tim Doan

# import libs
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
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        self.player = Player(self)
        # self.wall1 = Wall(WIDTH, 50, 0, HEIGHT, (200,250,200), "left")
        # self.wall2 = Wall(WIDTH, 50, 0, HEIGHT, (200,250, 200), "right")


        # self.all_sprites.add(self.wall1)
        # self.all_sprites.add(self.wall2)


        # self.walls.add(self.wall1)
        # self.walls.add(self.wall2)
        
        self.all_sprites.add(self.player)
        

        # for wall in WALL_LIST:
        #     w = Wall(*wall)
        #     self.all_sprites.add(w)
        #     self.walls.add(w)
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
        self.all_sprites.update()
        if self.player.pos.x < 75:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            self.player.vel.x = 1
            print("left wall")
        if self.player.pos.x > 725:
            hits = pg.sprite.spritecollide(self.player, self.walls, False)
            self.player.vel.x = -1
            print("right wall")


    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()