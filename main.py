import numpy as np
import matplotlib.pyplot as plt
from graph import Graph
import time
import random
#### Initialization
FewG = 32
ManyG = 256
CurrentG = FewG
NodeGroups = 3
#### Build the graph
graph = Graph(CurrentG * NodeGroups)
y = np.count_nonzero(np.random.binomial(1,1/2,10))
for i in range(NodeGroups * CurrentG):
    if(i == 0):
        NumberList = random.sample(range(0, CurrentG), y)
        for j in NumberList:
            graph.add_edge(i, j, 1)
    elif(i == NodeGroups - 1):
        NumberList = random.sample(range((i//CurrentG)*CurrentG, CurrentG*NodeGroups), y)
        for j in NumberList:
            graph.add_edge(i, j, 1)
    else:
        NumberList = random.sample(range(CurrentG*((i//CurrentG)-1), CurrentG*((i//CurrentG)+1)), y)
        for j in NumberList:
            graph.add_edge(i, j, 1)

graph.print_edge_matrix()
#### The algorithms


#### Output