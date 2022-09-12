#This is the code for hungarian algorithm on maximum matching problem
import numpy as np
from graph import Graph
from queue import Queue

def HungarianMaxMatching(graph):
    M = []
    for i in range(graph.num_of_nodes):
        S = []  # S is the vertexs that are already matched
        P = []
        Q = Queue()
        if graph.getDegree(i, 0) == 0: # if the vertex is isolated, then skip
            continue
        Q.put([i, 0])
        bestV = -1
        while not Q.empty():
            w = Q.get()
            S.append(w)
            if w[1] == 0:
                N = graph.getNeighbors(w[0], w[1], S)
            else:
                N = graph.getUnmatchedEdges(w[0], w[1], S)

            for n in N:
                if w[1] == 0:
                    if n[1] == 1:
                        if bestV == -1 or graph.getDegree(bestV, 1) < graph.getDegree(n[0], 1):#cunzai yijing match de neighbor
                            bestV = n[0]
                else:##for v, it needs to find a vertex not been searched and can match with someone else
                    if n not in S and graph.isMatched(n[0], n[1]):##ATTENTION
                        Q.put(n)
                        break

        if bestV == -1:
            P.append([i, N[0][0]])
        else:
            P.append([i, bestV])
            Q.put([bestV, 1])

        flag = False
        for p in P:
            if not flag:
                graph.add_edge(p[0], p[1], 1, 1)
                flag = True
            else:
                graph.add_edge(p[0], p[1], 1, 0)
                flag = False
    # build the matching M(indicator == 2)
    for i in range(graph.num_of_nodes):
        for j in range(graph.num_of_nodes):
            if graph.edge_matrix[i][j] == 2:
                M.append([i, j])
    #fin





