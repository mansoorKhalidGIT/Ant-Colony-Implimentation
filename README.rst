Python implementation of the Ant Colony system

Development
-----------

Install the requirements:

    pip install -r requirements.txt

Run tests:

    pytest --pep8

Usage
-----

    from ant_colony.graph import Node, Graph

    nodes = [Node(0, 0), Node(0, 1), Node(1, 1), Node(1, 0)]

    graph = Graph(nodes)

    path, distance = graph.find_shortest_path()

Output
-----
Path: [0, 1, 2, 3]
Distance: 4.0
