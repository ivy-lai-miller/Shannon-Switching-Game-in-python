import pygame
import sys
from pygame.locals import *


class Game:

    def __init__(self, fname):

        self.num_points = None
        self.links = {}
        self.special= []

        # Read in the file and give it points
        fptr= open(fname, "r").read()
        lines = fptr.split("\n")
        # TO DO read in the file

        for line in lines:
            # check if split
            line = line.split()
            # print line
            if len(line) ==0:
                continue
            if line[0] == "P":
                self.num_points = int(line[1])
                self.links[self.num_points] = []
            if line[0] == "L":
                check1 = int(line[1])
                check2 = int(line[2])
                num_links = int(line[3])
                x = 0
                while x <= num_links:
                    self.links[check1] = check2
                    self.links[check2] = check1
                    x+=1

            if line[0] == "S":
                self.special.append(line[1])
                self.special.append(line[2])

        # FOR TESTING
        print "Number of points: %d" %self.num_points
        print "Dictionary of links: %s"  % self.links
        print "Special points: %s" % self.special

    def win_status(self):
        if len(self.special) == 1:
            return True

    def run(self):
        pass

a = Game("sample_input.txt")








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
x = round(sin(2*3.14/N_points))
pygame.draw.circle(DISPLAYSURF,BLUE, (300,50), 5, 0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
