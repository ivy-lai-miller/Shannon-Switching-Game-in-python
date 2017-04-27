import pygame
import sys
from pygame.locals import *

class Game:

    def __init__(self, fname):
        # Read in the file and give it points
        fptr= open(fname, "r").read()
        lines = fptr.split("\n")


# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,800))
# pygame.display.init()
pygame.display.set_caption("Hello World!")


DISPLAYSURF.fill(WHITE)
# circle(Surface, color, pos, radius, width=0)
pygame.draw.circle(DISPLAYSURF,BLUE, (300,50), 5, 0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
