def depth_first_search(graph, start, visited=None):
    """
    Perform Depth First Search (DFS) on a graph.

    Parameters:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      Each key is a vertex, and the value is a list of neighbors.
        start (any): The starting vertex for the DFS.
        visited (set): A set to keep track of visited vertices.

    Returns:
        list: A list of vertices in the order they are visited.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(depth_first_search(graph, neighbor, visited))

    return result

