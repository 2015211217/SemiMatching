import numpy as np
import queue
import sys

def InitialSemiMatching(graph):
    M = []
    DegreeU = []
    for i in range(graph.num_of_nodes):
        DegreeU.append([graph.getDegree(i, 0), i])
    np.sort(DegreeU)
    for u in DegreeU:
        minDegreeNeighbor = sys.maxsize
        for j in range(graph.num_of_nodes):
            if(graph.edge_matrix[j][u[1]]!=0):
                if (graph.getDegree(j, 1) < minDegreeNeighbor):
                    minDegreeNeighbor = graph.getDegree(j, 1)
        M.append([u[0], minDegreeNeighbor])
    return M

def DoDepthFirstSearch(graph, root, S):
    MatchedNeighberV = graph.getMatchedVertex(1)
    for u in MatchedNeighberV:
        ##let parentU = root
        for k in range(0, graph.num_of_nodes):
            if graph.edge_matrix[u[0]][k] == 2:
                graph.delete_edge(u[0], k)
        graph.add_edge(u[0], root, 1, 1)
        UnMatchedNeightberV = graph.getUnmatchedVertex(0)
        for w in UnMatchedNeightberV:
            if S[w[0]]==-1 or graph.getDegree(w[0], 0) > graph.getDegree(root, 1):
                continue
            S[w[0]] = -1
            ## Let parent(w) = u
            for k in range(0, graph.num_of_nodes):
                if graph.edge_matrix[w[0]][k] == 1:
                    graph.delete_edge(w[0], k)
            graph.add_edge(u[0], w[0], 1, 0)
            if graph.getDegree(w[0], 1) <= graph.getDegree(root, 1) - 2:
                break
            DoDepthFirstSearch(graph, w[0], S)

def AlgorithmSm2(graph):
    ## Compute the initial semi-matching
    M = InitialSemiMatching(graph)
    ## FindCostReducingPath
    S = [1] * graph.num_of_nodes

    DegreeS = []
    for i in range(0, graph.num_of_nodes):
        DegreeS.append(graph.getDegree(i, 1))
    root = np.argmax(DegreeS)
    S[root] = -1
    for i in range(0, root + 1):
        graph.delete_edge(i, root)
    DoDepthFirstSearch(graph, root, S)
