# File by Tim Doan  

# screen dimensions
WIDTH = 1000
HEIGHT = 750

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
GREEN = (0,255,0)

# game settings
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# player settings
PLAYER_ACC = 0.88
PLAYER_FRICTION = -1
PLAYER_GRAV = 0.8

# wall settings
WALL_LIST = [((0, 0, 25, 750, BLACK, "left")), (WIDTH - 25, 0, 25, 750, BLACK, "right")]

# roof settings
ROOF_LIST = [((0, 0, 1000, 25, BLACK, "top")), (0, HEIGHT - 25, 1000, 25, BLACK, "bottom")]