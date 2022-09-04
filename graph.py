import numpy as np

class Graph():

    def __init__(self, num_of_nodes, directed = False):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.edge_matrix = [[0 for _ in range(num_of_nodes)] for _ in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight, direction):
        self.edge_matrix[node1][node2] = weight + direction # direction = 0 : node1->node2 ; direction = 1 : node2->node1

    def delete_edge(self, node1, node2):
        self.edge_matrix[node1][node2] = 0

    def print_edge_matrix(self):
        for i in range(self.num_of_nodes) :
            print(self.edge_matrix[i])

    def getLineAndRow(self):
        return self.num_of_nodes

    def getMatchedVertex(self, node1, indicator):
        N = []
        M = [i for i, x in enumerate(self.edge_matrix[node1]) if x == 1]
        for i in M:
            N.append([i, indicator])
        return N

    def getUnmatchedVertex(self, node1, indicator):
        N = []
        M = [i for i, x in enumerate(self.edge_matrix[node1]) if x == 0]
        for i in M:
            N.append([i, indicator])
        return N

    def getDegree(self, node, indicator):
        if node < 0 or node >= self.num_of_nodes:
            return -1
        elif (indicator == 0):# 0 is line, 1 is row
            return np.count_nonzero(self.edge_matrix[node])
        elif (indicator == 1):
            count = 0
            for i in range(self.num_of_nodes):
                if self.edge_matrix[i][node] == 1:
                    count += 1
            return count
        else:
            print("Error: invalid indicatior!")


    def getParent(self, nodeWithIndi):
        if nodeWithIndi[1] == 1: #find a prent for V
            for i in range(0, nodeWithIndi[0] + 1):
                if self.edge_matrix[nodeWithIndi[0] - i][nodeWithIndi[0]] == 1:
                    return nodeWithIndi[0] - i
        elif nodeWithIndi[1] == 0:
            for i in range(0, nodeWithIndi[0] + 1):
                if self.edge_matrix[nodeWithIndi[0]][nodeWithIndi[0]-i] == 2:
                    return nodeWithIndi[0] - i
        print("Error: no parent found!")