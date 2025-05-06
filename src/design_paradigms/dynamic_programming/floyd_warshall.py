def floyd_warshall(graph):
    """
    Perform the Floyd-Warshall algorithm to find the shortest paths
    between all pairs of vertices in a weighted graph.

    Parameters:
        graph (list of list of int): A 2D list representing the adjacency matrix
                                     of the graph. graph[i][j] is the weight of
                                     the edge from vertex i to vertex j, or float('inf')
                                     if there is no edge.

    Returns:
        list of list of int: A 2D list where the value at [i][j] represents the
                             shortest distance from vertex i to vertex j.
    """
    # Number of vertices in the graph
    n = len(graph)

    # Initialize the distance matrix with the input graph
    dist = [row[:] for row in graph]

    # Update the distance matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update the shortest distance from i to j through vertex k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
# if __name__ == "__main__":
#     # Define the graph as an adjacency matrix
#     # Use float('inf') to represent no direct edge between vertices
#     graph = [
#         [0, 3, float('inf'), 5],
#         [2, 0, float('inf'), 4],
#         [float('inf'), 1, 0, float('inf')],
#         [float('inf'), float('inf'), 2, 0]
#     ]

#     result = floyd_warshall(graph)
#     print("Shortest distances between every pair of vertices:")
#     for row in result:
#         print(row)