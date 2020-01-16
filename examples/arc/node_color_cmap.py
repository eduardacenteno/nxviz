"""
Displays different node_color based on a provided cmap with ArcPlot
"""

import matplotlib.pyplot as plt
import networkx as nx
from nxviz.plots import ArcPlot

G = nx.Graph()

G.add_node("A", type="Alpha")
G.add_node("B", type="Beta")
G.add_node("C", type="Alpha")


G.add_edge("A", "B", weight=8)
G.add_edge("A", "C", weight=8)
G.add_edge("B", "C", weight=8)


c = ArcPlot(G, node_color="type", node_cmap="Set1", edge_width="weight")

c.draw()
plt.show()
