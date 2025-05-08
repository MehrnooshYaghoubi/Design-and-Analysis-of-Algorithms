from collections import deque

def breadth_first_search(graph, start):
    """
    Perform Breadth First Search (BFS) on a graph.

    Parameters:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      Each key is a vertex, and the value is a list of neighbors.
        start (any): The starting vertex for the BFS.

    Returns:
        list: A list of vertices in the order they are visited.
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

