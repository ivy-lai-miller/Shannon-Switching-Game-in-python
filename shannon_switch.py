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

        for line in lines:
            line = line.split()

            #check for blank lines and skip
            if len(line) ==0:
                continue

            # Specify points/nodes
            if line[0] == "P":
                try:
                    self.num_points = int(line[1])
                except:
                    print "Number of nodes specified incorrectly."
                    sys.exit(1)

            # Check for links
            if line[0] == "L":
                # If number of same links between nodes are specified, make that many instances of the connection
                if len(line) > 3:
                    for counter in range(int(line[3])):
                        self.links.append((int(line[1]), int(line[2])))
                else:
                    try:
                        self.links.append((int(line[1]), int(line[2])))
                    except:
                        print "Link is specified incorrectly."
                        sys.exit(1)

            if line[0] == "S":
                if len(line) < 3:
                    print "Error in specifying special nodes."
                    sys.exit(1)
                else:
                    self.special.append(int(line[1]))
                    self.special.append(int(line[2]))


        if self.num_points == None or self.num_points == 0:
            print "Points not specified"
            sys.exit(1)
        if len(self.special) < 2:
            print "Special Nodes not defined."
            sys.exit(1)
        if len(self.links) ==0:
            print "No links are defined."
            sys.exit(1)

    # Print function for debugging
    def prnt(self):
        print "Number of points: %d" %self.num_points
        print "Number of links: %d" %len(self.links)
        print "Special Nodes are: %d, %d" %(self.special[0], self.special[1])

    def run(self):
        # Set up the networkx graph/board
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

            if status == "CUT":
                print "\nCUT's move. Type EXIT to end. a b to delete the edge between a and b."
                raw = raw_input("What would you like to do? ")
                # pass

            if raw.upper() == "EXIT":
                playing = False
                continue

            if raw.upper() == "SHOW BOARD":
                continue


                # check if a move is valid
            else:
                if status == "SHORT":
                # If you SHORT, the  two points merge
                # Update connections
                # Make sure you also update the status now to SHORT
                    c, d = map(int, raw.split())
                    try:
                        if d in self.special:
                            c,d = d,c
                        # contracted_edge
                        G=nx.contracted_edge(G,(c,d))
                        if (c==self.special[0] and d==self.special[1]) or (c==self.special[1] and d==self.special[0]):
                            print "Short wins"
                            playing=False
                        else:
                            status= "CUT"
                            continue
                        print "if there is an exception this shouldnt print"
                    except:
                        print "Bad input!"

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
                            continue

                    except:
                        # continue
                        print "Bad input!"


        print "Bye!"

# Use argv to load in the input file
if len(sys.argv)<= 1:
    print "Include file name in command line."
else:
    test = Game(sys.argv[1])
    # test.prnt()
    test.run()
