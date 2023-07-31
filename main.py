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


def DFS_Traversal(graph, v, visited, parent_node=-1):
    # assign current node as
    visited[v] = True

    # loop for every edge (v, u)
    for u in graph.adjacencyList[v]:

        # if `u` is not visited
        if not visited[u]:
            if DFS_Traversal(graph, u, visited, v):
                return True

        # if `u` is visited, and `u` is not a parent_node
        elif u != parent_node:
            # found a back-edge
            return True

    # No back-edges were found
    return False

if __name__ == '__main__':
    # List of graph edges
    edges = [
        ("A", "B"), ("A", "C"), ("C", "B"), ("C", "E"), ("D", "E")
    ]

    # construct graph
    constructed_graph = Graph(edges)

    # note the visited and unvisited nodes
    visited = {}
    for key in constructed_graph.adjacencyList:
        visited[key] = False

    if DFS_Traversal(constructed_graph, "E", visited):
        print('Cycle detected')
    else:
        print('Cycle not detected')