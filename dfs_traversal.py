class Graph:

    def __init__(self, edges):
        # Adjacency list representation
        self.adjacencyList = {}

        for (source, destination) in edges:
            if source not in self.adjacencyList:
                self.adjacencyList[source] = [destination]
            else:
                self.adjacencyList[source] += destination
            if destination not in self.adjacencyList:
                self.adjacencyList[destination] = [source]
            else:
                self.adjacencyList[destination] += source


def DFS_Traversal(graph, v, visited):
    # assign current node as

    if not visited[v]:
        visited[v] = True
        print(v)

        for u in graph.adjacencyList[v]:
            DFS_Traversal(graph, u, visited)


if __name__ == '__main__':
    # List of graph edges
    edges = [
        ("A", "B"), ("A", "C"), ("C", "B"), ("C", "E"), ("D", "E"), ("A", "D")
    ]

    # construct graph
    constructed_graph = Graph(edges)

    # note the visited and unvisited nodes
    visited = {}
    for key in constructed_graph.adjacencyList:
        visited[key] = False

DFS_Traversal(constructed_graph, "A", visited)
