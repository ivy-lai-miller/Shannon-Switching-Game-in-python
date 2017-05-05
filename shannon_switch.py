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

            # Check for blank lines and skip
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

            # Store which nodes are special
            if line[0] == "S":
                if len(line) < 3:
                    print "Error in specifying special nodes."
                    sys.exit(1)
                else:
                    self.special.append(int(line[1]))
                    self.special.append(int(line[2]))


        # Print if there is an error in specifying the game
        if self.num_points == None or self.num_points == 0:
            print "Points not specified"
            sys.exit(1)
        if len(self.special) < 2:
            print "Special Nodes not specified."
            sys.exit(1)
        if len(self.links) ==0:
            print "No links are specified."
            sys.exit(1)

    # Print function for debugging
    def prnt(self):
        print "Number of points: %d" %self.num_points
        print "Number of links: %d" %len(self.links)
        print "Special Nodes are: %d, %d" %(self.special[0], self.special[1])


    # Run function to play the game
    def run(self):
        # Set up the networkx graph/board
        G = nx.MultiGraph()
        G.add_node(self.num_points)
        G.add_edges_from(self.links)
        status = None

        # Color all nodes blue except for special nodes which are red
        for node in G.node:
            # red nodes are special
            if node not in self.special:
                G.node[node]["fill"] = "blue"

        # Designate which mode Player 1 will be
        first = raw_input("Who do you want to go first? Type SHORT or CUT>> ")
        if first.upper() == "SHORT":
            status = "SHORT"
        elif first.upper() == "CUT":
            status = "CUT"
        else:
            print "Bad input"
            sys.exit(1)

        playing = True

        # Once user has chosen the mode, start playing the game
        while playing:

            # Display the network using NetworkX Viewer for each loop
            Viewer(G).mainloop()

            # Display text to user and prompt for a move
            # the user input is stored in raw
            if status == "SHORT":
                print "\nSHORT's move. Type EXIT to end. a b to short the edge between a and b."
                raw = raw_input("What would you like to do? ")

            if status == "CUT":
                print "\nCUT's move. Type EXIT to end. a b to delete the edge between a and b."
                raw = raw_input("What would you like to do? ")

            # option to exit the game
            if raw.upper() == "EXIT":
                playing = False
                continue

            # option to display the board if the user forgets or closes by accident
            if raw.upper() == "SHOW BOARD":
                continue


            # play with the user input, which should be two integers
            else:
                if status == "SHORT":

                    try:
                        # maps the user input to two integers c,d
                        c, d = map(int, raw.split())

                        # switch the two values to keep the special node
                        # This is because contracted edge technically merges second node into the first node
                        if d in self.special:
                            c,d = d,c

                        # contracted_edge(network, location as tuple)
                        G = nx.contracted_edge(G,(c,d))

                        # If the code gets to this point, that means c and d are indeed connected
                        # Then we should see if we shorted the link between two special points
                        # If so, then we win!
                        if c in self.special and d in self.special:
                            print "Short wins"
                            playing=False

                        # Otherwise, it's the next player's turn
                        else:
                            status= "CUT"
                        continue
                    # If anything fails, then catch exception
                    except:
                        print "Bad input!"

                if status == "CUT":
                    # If you cut, the connection is gone

                    try:
                        a, b = map(int, raw.split()) #this works there just has to be a space between the two numbers
                        G.remove_edge(a,b)

                        # Check if there is any path between the two special points
                        # If not, cut wins!
                        if (nx.has_path(G,self.special[0],self.special[1])==False):
                            print "Cut wins"
                            playing= False

                        else:
                            # Next player's move
                            status="SHORT"
                        continue

                    except:
                        print "Bad input!"


        print "Bye!"

# Use argv to load in the input file
if len(sys.argv)<= 1:
    print "Include file name in command line."
else:
    test = Game(sys.argv[1])
    # test.prnt()
    test.run()
