from graph import Graph

graph = Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

graph.add_edge("A", "B", 5)
graph.add_edge("B", "C", 10)
graph.add_edge("A", "C", 7)

graph.add_edge("A", "D", 8)

print(graph.adjacency_list)
