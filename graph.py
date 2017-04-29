import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.connectivity as cn
from networkx_viewer import Viewer

# Create an empty graph.
G = nx.Graph()

# Add 4 nodes.
G.add_nodes_from([0,1,2,3])
G.node[0]["fill"] = "blue"

# Add edges making the graph a circle.
G.add_edges_from([(0,1),(1,2),(2,3),(3,0)])

playing = True

while playing:
    # Show the user the current state of the graph.
    #nx.draw_networkx(G)
    #plt.show()
    Viewer(G).mainloop()

    foo = raw_input("Type EXIT to end, a b to delete the edge between a and b: ")
    if foo == "EXIT":
        playing = False
    else:
        a, b = map(int, foo.split())
        try:
            G.remove_edge(a,b)
        except:
            print "Bad input!"
    if cn.local_edge_connectivity(G,0,2):
        print "Still connected!"
    else:
        print "Graph split, you won!"
        playing = False

print "Bye!"

