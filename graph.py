import numpy as np

class Graph():

    def __init__(self, num_of_nodes, directed = False):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.edge_matrix = [[0 for _ in range(num_of_nodes)] for _ in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight, direction):
        if node1 >= self.num_of_nodes or node2 >= self.num_of_nodes:
            print("Error: exceed the limit!!")
            exit(0)
        self.edge_matrix[node1][node2] = weight + direction # direction = 0 : node1->node2 ; direction = 1 : node2->node1

    def delete_edge(self, node1, node2):
        self.edge_matrix[node1][node2] = 0

    def print_edge_matrix(self):
        for i in range(self.num_of_nodes) :
            print(self.edge_matrix[i])

    def getLineAndRow(self):
        return self.num_of_nodes

    def getMatchedVertex(self, indicator): ## modification needed
        N = []
        M = []
        if indicator == 1:
            for i in range(self.num_of_nodes):
                for j in range(self.num_of_nodes):
                    if self.edge_matrix[i][j] == 2:
                        M.append(i)
                        break
        elif indicator == 0:
            for i in range(self.num_of_nodes):
                for j in range(self.num_of_nodes):
                    if self.edge_matrix[j][i] == 2:
                        M.append(i)
                        break
        for i in M:
            N.append([i, np.abs(indicator - 1)])
        return N

    def getUnmatchedVertex(self, indicator):
        N = []
        M = []
        if indicator == 1:
            for i in range(self.num_of_nodes):
                for j in range(self.num_of_nodes):
                    if self.edge_matrix[i][j] == 2:
                        M.append(i)
                        break
        elif indicator == 0:
            for i in range(self.num_of_nodes):
                for j in range(self.num_of_nodes):
                    if self.edge_matrix[j][i] == 2:
                        M.append(i)
                        break

        for i in range(self.num_of_nodes):
            if i not in M:
                N.append([i, np.abs(indicator - 1)])
        return N

    def getDegree(self, node, indicator):
        if node < 0 or node >= self.num_of_nodes:
            return -1
        elif indicator == 0:# 0 is line, 1 is row
            count = 0
            for i in range(self.num_of_nodes):
                if self.edge_matrix[node][i] == 2:
                    count += 1
            return count
        elif indicator == 1:
            count = 0
            for i in range(self.num_of_nodes):
                if self.edge_matrix[i][node] == 2:
                    count += 1
            return count
        else:
            return -1

    def getParent(self, nodeWithIndi):
        if nodeWithIndi[1] == 1: #find a parent for V
            for i in range(0, self.num_of_nodes):
                if self.edge_matrix[i][nodeWithIndi[0]] == 1:
                    return i
        elif nodeWithIndi[1] == 0:
            for i in range(0, self.num_of_nodes):
                if self.edge_matrix[nodeWithIndi[0]][i] == 2:
                    return i
        self.print_edge_matrix()
        print("Error: no parent found!")