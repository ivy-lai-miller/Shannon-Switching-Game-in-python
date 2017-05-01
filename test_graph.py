import sys
# from pygame.locals import *
import math
import networkx as nx
from networkx_viewer import Viewer
import networkx.algorithms.connectivity as con

G = nx.MultiGraph()
G.add_node(10)
G.add_edges_from([(1,2),(2,3), (3,4)])
status = None

for node in G.node:
    if node not in [1,2]:
        G.node[node]["fill"] = "blue"

status = "SHORT"
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
