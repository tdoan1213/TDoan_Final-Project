# File by Tim Doan  

# screen dimensions
WIDTH = 1000
HEIGHT = 750

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)
BLUE = (50,50,255)
RED = (255,50,50)
GREEN = (0,255,0)

# game settings
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False


# wall settings
WALL_LIST = [((0, 0, 25, 750, WHITE, "left")), (WIDTH - 25, 0, 25, 750, WHITE, "right")]

# roof settings
ROOF_LIST = [((0, 0, 1000, 25, WHITE, "top")), (0, HEIGHT - 25, 1000, 25, WHITE, "bottom")]
