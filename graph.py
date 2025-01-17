class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = {}
        else:
            print(f"Node {node} already exists.")