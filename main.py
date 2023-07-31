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

        self.a = len(self.adjacencyList)


if __name__ == '__main__':
    # List of graph edges
    edges = [
        ("A", "B"), ("A", "C"), ("C", "B"), ("C", "E"), ("D", "E")
    ]

    # construct graph
    constructed_graph = Graph(edges)

    # note the visited and unvisited nodes
    visited = [False] * constructed_graph.a

    print(constructed_graph.adjacencyList)
