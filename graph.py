
class Graph():

    def __init__(self, num_of_nodes, directed = True):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.edge_matrix = [[0 for _ in range(num_of_nodes)] for _ in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight):
        self.edge_matrix[node1][node2] = weight
        if not self