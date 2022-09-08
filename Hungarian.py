#This is the code for hungarian algorithm on maximum matching problem
import numpy as np
from graph import Graph
from queue import Queue

def HungarianMaxMatching(graph):
    #at the beginning, all the nodes are unmatched
    #maintain two vectors that indicates the situation
    #isolated or not???
    M = []
    S = []
    for i in range(graph.num_of_nodes):
        Q = Queue()
        if graph.getDegree(graph, i, 0) == 0: # if the vertex is isolated, then skip
            continue
        Q.put([i, 0])
        while not Q.empty():
            w = Q.get()
            N = []
            if w[1] == 0: #w is in the left side
                N = graph.getUnmatchedNeighbor(graph, w[0], )
            else:

