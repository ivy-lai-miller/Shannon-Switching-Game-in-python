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

            if line[0] == "S":
                self.special.append(int(line[1]))
                self.special.append(int(line[2]))


    def run(self):
        G = nx.MultiGraph()
        G.add_node(self.num_points)
        G.add_edges_from(self.links)
        status = None

        for node in G.node:
            # red nodes are special
            if node not in self.special:
                G.node[node]["fill"] = "blue"

        first = raw_input("Who do you want to go first? Type SHORT or CUT>> ")
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
                    if d in self.special:
                        c,d = d,c
                    # contracted_edge
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


        print "Bye!"



if len(sys.argv)<= 1:
    print "Include file name in command line."
else:
    test = Game(sys.argv[1])
    # a.prnt()
    test.run()
