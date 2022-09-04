import numpy as np
import matplotlib.pyplot as plt
from graph import Graph
import datetime
import random
from AlgorithmSm1 import AlgorithmSm1
from AlgorithmSm2 import AlgorithmSm2

#### Initialization
FewG = 5
ManyG = 256
CurrentG = FewG
NodeGroups = 2
#### Build the graph
graph = Graph(CurrentG * NodeGroups)
y = np.count_nonzero(np.random.binomial(1,1/2,10))
for i in range(NodeGroups * CurrentG):
    if(i == 0):
        NumberList = random.sample(range(0, CurrentG), y)
        for j in NumberList:
            graph.add_edge(i, j, 1, 0)
    elif(i == NodeGroups - 1):
        NumberList = random.sample(range((i//CurrentG)*CurrentG, CurrentG*NodeGroups), y)
        for j in NumberList:
            graph.add_edge(i, j, 1, 0)
    else:
        NumberList = random.sample(range(CurrentG*((i//CurrentG)-1), CurrentG*((i//CurrentG)+1)), y)
        for j in NumberList:
            graph.add_edge(i, j, 1, 0)
#graph.print_edge_matrix()

#### The algorithms
StartTime = datetime.datetime.now()
AlgorithmSm1(graph)
EndTime = datetime.datetime.now()
Ag1Time = EndTime-StartTime
print(Ag1Time)

StartTime = datetime.datetime.now()
AlgorithmSm2(graph)
EndTime = datetime.datetime.now()
Ag2Time = EndTime-StartTime
print(Ag2Time)


#### Output