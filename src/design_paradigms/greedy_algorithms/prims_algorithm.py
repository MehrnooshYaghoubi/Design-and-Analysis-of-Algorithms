import heapq

def prims_algorithm(graph, start):
    """
    Perform Prim's Algorithm to find the Minimum Spanning Tree (MST) of a graph.

    Parameters:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      Each key is a vertex, and the value is a list of tuples (neighbor, weight).
        start (any): The starting vertex for the algorithm.

    Returns:
        list: A list of edges in the MST, where each edge is represented as (u, v, weight).
    """
    mst = []  # List to store the edges of the MST
    visited = set()  # Set to track visited vertices
    min_heap = [(0, start, None)]  # Min-heap to store edges (weight, current_vertex, parent_vertex)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)

        # If the edge is not the starting vertex, add it to the MST
        if parent is not None:
            mst.append((parent, current, weight))

        # Add all edges from the current vertex to the heap
        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 5)],
        'B': [('A', 1), ('C', 4), ('D', 2)],
        'C': [('A', 5), ('B', 4), ('D', 6)],
        'D': [('B', 2), ('C', 6), ('E', 3)],
        'E': [('D', 3)]
    }

    start_vertex = 'A'
    mst = prims_algorithm(graph, start_vertex)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")