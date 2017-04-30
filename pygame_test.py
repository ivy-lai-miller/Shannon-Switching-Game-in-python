# import pygame
import sys
# from pygame.locals import *
import math
import networkx as nx
from networkx_viewer import Viewer
import networkx.algorithms.connectivity as con

class Game:

    def __init__(self, fname):

        self.num_points = None
        self.links = []
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
                # self.links[self.num_points] = []
            if line[0] == "L":
                for counter in range(int(line[3])):
                    self.links.append((int(line[1]), int(line[2])))
                # For Dictionary
                # check1 = int(line[1])
                # check2 = int(line[2])
                # num_links = int(line[3])
                # x = 0
                # while x <= num_links:
                #     self.links[check1] = check2
                #     self.links[check2] = check1
                #     x+=1

            if line[0] == "S":
                self.special.append(int(line[1]))
                self.special.append(int(line[2]))

        # FOR TESTING
        print "Number of points: %d" %self.num_points
        print "Array of links: %s"  % self.links
        print "Special points: %s" % self.special

    def win_status(self):
        if len(self.special) == 1:
            return True


    def lose(self):

        # If no more possible path between special nodes, then you lose
        pass

    # def show_board(self):
    #     G = nx.MultiGraph()
    #     G.add_node(self.num_points)
    #     G.add_edges_from(self.links)
    #
    #     for node in G.node:
    #         # red nodes are special
    #         if node not in self.special:
    #             G.node[node]["fill"] = "blue"
    #
    #     # shows the localal
    #     print con.local_node_connectivity(G, 1,2)
    #     # G.add_edge('0','2')
    #     # G.node['0']["outline"] = "blue"
    #     # G.node['2']["outline"] = "blue"
    #
    #     # G.add_node(self.num_points)
    #     # G.add_edge(lower,upper)



        app = Viewer(G)
        app.mainloop()

    def run(self):
        G = nx.MultiGraph()
        G.add_node(self.num_points)
        G.add_edges_from(self.links)
        status = None

        for node in G.node:
            # red nodes are special
            if node not in self.special:
                G.node[node]["fill"] = "blue"

        first = raw_input("Who do you want to go first? Type SHORT or CUT>>")
        if first.upper() == "SHORT":
            status = "SHORT"
        elif first.upper() == "CUT":
            status = "CUT"
        else:
            print "Bad input"
            sys.exit(1)

        playing = True

        while playing:

            Viewer(G).mainloop()

            if status == "SHORT":
                print "\nSHORT's move. Type EXIT to end. a b to short the edge between a and b."
                raw = raw_input("What would you like to do? ")
                # pass

            if status.upper() == "CUT":
                print "\nCUT's move. Type EXIT to end. a b to delete the edge between a and b."
                raw = raw_input("What would you like to do? ")
                # pass

            # raw = raw_input("Type EXIT TO end")
            if raw == "EXIT":
                playing = False
            else:
                if status == "SHORT":
                # If you SHORT, the  two points merge
                # Update connections
                # Make sure you also update the status now to SHORT
                    c, d = map(int, raw.split())
                    G=nx.contracted_edge(G,(c,d))
                    if (c==self.special[0] and d==self.special[1]) or (c==self.special[1] and d==self.special[0]):
                        print "Short wins"
                        playing=False
                    else:
                        status= "CUT"

                if status == "CUT":
                    # If you cut, the connection is gone
                    # Make sure you also update the status now to SHORT
                    a, b = map(int, raw.split()) #this works there just has to be a space between the two numbers
                    try:
                        G.remove_edge(a,b)
                        if (nx.has_path(G,self.special[0],self.special[1])==False):
                            print "Cut wins"
                            playing= False
                        else:
                            status="SHORT"
                        
                    except:
                        continue
                        #print "Bad input!"
                
                #if status=="SHORT" and G.has_edge(self.special[0],self.special[1])==True:
                    #print "Short wins"
                    #playing =False
                # if con.local_edge_connectivity(G,0,2):
                #     print "Still connected!"
                #else:
                    #print "Graph split, you won!"
                    #playing = False

        print "Bye!"




test = Game("sample_input.txt")
test.run()

# TRASH
# class Point:
#
#     def __init__(self, special = False, name = 0):
#         self.special = special
#         self.name = name
#
# class Link:
#     def __init__(self, point1, point2):
#         lower = min(point1.name, point2.name)
#         higher = max(point1.name, point2.name)







'''
# PYGAME STUFF
# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((300,300))
# pygame.display.init()
pygame.display.set_caption("Hello World!")


DISPLAYSURF.fill(WHITE)
# circle(Surface, color, pos, radius, width=0)

circle_location = []
counter = 0
while counter <=test.num_points:
    # TO DO: SCALING
    y = int(round(math.sin(2*3.14/test.num_points*counter)))*60+100
    # print (2*3.14/test.num_points*counter)
    x = int(round(math.cos(2*3.14/test.num_points*counter)))*60 +100
    pygame.draw.circle(DISPLAYSURF,BLUE, (x,y), 6, 0)
    counter +=1
    circle_location.append((x,y))

for link in test.links:


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
'''
