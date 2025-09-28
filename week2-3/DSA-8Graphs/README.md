📊 Graphs in Python – Pathfinding & Shortest Path

This module demonstrates how to represent and work with Graphs in Python using an adjacency list approach.
Graphs are fundamental data structures widely used in networking, maps, AI, recommendation systems, and many real-world applications.

🚀 What I Implemented
1. Graph Representation (Adjacency List)

Created a graph using a dictionary (graph_dict) where each key is a node, and values are its connected neighbors.

Input was taken as edges (start → end pairs).

routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

2. All Paths Between Two Nodes

Implemented get_paths(start, end) to recursively explore all possible paths.

Used DFS (Depth First Search) approach to avoid revisiting nodes.

✅ Example:

route_graph.get_paths("Mumbai", "New York")


Output:

[['Mumbai', 'Paris', 'New York'], 
 ['Mumbai', 'Paris', 'Dubai', 'New York'], 
 ['Mumbai', 'Dubai', 'New York']]

3. Shortest Path Between Two Nodes

Implemented get_shortest_path(start, end) to recursively find the smallest path length.

Compared candidate paths and returned the shortest one.

✅ Example:

route_graph.get_shortest_path("Mumbai", "New York")


Output:

['Mumbai', 'Paris', 'New York']

🧠 Key Learnings

Graphs are everywhere – from flight routes to social networks.

Adjacency lists are memory-efficient compared to adjacency matrices.

Recursive DFS-based pathfinding helps explore all routes.

Shortest path can be derived by comparing path lengths (intro to BFS/Dijkstra in future).