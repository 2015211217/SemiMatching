import numpy as np
from queue import Queue


def AlgorithmSm1(graph):
    M = []
    for i in range(graph.getLineAndRow()): #all the vertex at i
        Q = Queue()
        bestV = -1
        Q.put([i,0])# 0 = U; 1 = V
        while(Q.empty() == False):
            w = Q.get()
            N = []

            if (w[1] == 0):
                N = graph.getMatchedVertex(w[0], w[1])  # N is in U
            else:
                N = graph.getUnmatchedVertex(w[0], w[1])  # N is in V
                if (bestV == -1 or graph.getDegree(w[0],1) < graph.getDegree(bestV, 1)):
                    bestV = w[0]
            for n in N:
                if n[1] == 0:
                    ##delete all the edges point at n[0]
                    for k in range(0, graph.num_of_nodes):
                        if graph.edge_matrix[n[0]][k] == 2:
                            graph.delete_edge(n[0], k)
                    graph.add_edge(n[0], w[0], 1, 1)
                elif n[1] == 1:
                    for k in range(0, graph.num_of_nodes):
                        if graph.edge_matrix[n[0]][k] == 1:
                            graph.delete_edge(n[0], k)
                    graph.add_edge(n[0], w[0], 1, 0)
                else:
                    print("Error: Invalid index value!")
                Q.put(n)
        v = bestV
        u = graph.getParent([v, 1])
        M.append([u, v])
        while u != i:
            v = graph.getParent([u, 0])
            graph.delete_edge(u, v)
            u = graph.getParent([v, 0])
            M.append([u, v])