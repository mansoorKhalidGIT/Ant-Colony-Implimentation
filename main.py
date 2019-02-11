from ant_colony.graph import Node, Graph

nodes = [Node(0, 0), Node(0, 1), Node(1, 1), Node(1, 0)]

graph = Graph(nodes)

path, distance = graph.find_shortest_path()
print("Path:")
print(path)
print("Distance:")
print(distance)