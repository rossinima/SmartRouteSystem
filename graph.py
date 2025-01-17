class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = {}
        else:
            print(f"Node {node} already exists.")
        
    def add_edge(self, node1, node2, weight):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1][node2] = weight
            self.adjacency_list[node2][node1] = weight 
        else: 
            print(f"One or both nodes {node1}, {node2} do not exist.")