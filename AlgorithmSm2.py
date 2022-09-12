import numpy as np
import queue
import sys

def InitialSemiMatching(graph):
    DegreeU = []
    for i in range(graph.num_of_nodes):
        DegreeU.append([graph.getDegreeM(i, 0), i])
    np.sort(DegreeU)
    for u in DegreeU:
        minDegreeNeighbor = 0
        minDegree = sys.maxsize
        for j in range(graph.num_of_nodes):
            if(graph.edge_matrix[j][u[1]]!=0):
                if (graph.getDegreeM(j, 1) < minDegree):
                    minDegree = graph.getDegreeM(j, 1)
                    minDegreeNeighbor = j
        graph.add_edge(u[0], minDegreeNeighbor, 1, 1)

def DoDepthFirstSearch(graph, root, S):
    MatchedNeighberV = graph.getMatchedNeighborsOfV(root, []) #get matched Neighbors of v
    for u in MatchedNeighberV:
        ##let parentU = root
        for k in range(0, graph.num_of_nodes):
            if graph.edge_matrix[u][k] == 2:
                graph.delete_edge(u, k)
        graph.add_edge(u, root, 1, 1)
        UnMatchedNeightberV = graph.getUnmatchedNeighborsOfU(u, [])#get unmatched neighbors of U

        for w in UnMatchedNeightberV:
            if S[w[0]]==-1 or graph.getDegreeM(w[0], 0) > graph.getDegreeM(root, 1):
                continue
            S[w[0]] = -1
            ## Let parent(w) = u
            for k in range(0, graph.num_of_nodes):
                if graph.edge_matrix[w[0]][k] == 1:
                    graph.delete_edge(w[0], k)
            graph.add_edge(u[0], w[0], 1, 0)
            if graph.getDegreeM(w[0], 1) <= graph.getDegreeM(root, 1) - 2:
                break
            DoDepthFirstSearch(graph, w[0], S)

def AlgorithmSm2(graph):
    ## Compute the initial semi-matching
    InitialSemiMatching(graph)
    ## FindCostReducingPath
    S = [1] * graph.num_of_nodes

    DegreeS = []
    for i in range(0, graph.num_of_nodes):
        DegreeS.append(graph.getDegreeM(i, 1))
    root = np.argmax(DegreeS)
    S[root] = -1
    for i in range(0, root + 1):
        graph.delete_edge(i, root)
    DoDepthFirstSearch(graph, root, S)
