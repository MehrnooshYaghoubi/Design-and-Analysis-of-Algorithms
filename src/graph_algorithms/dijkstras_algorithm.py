import heapq

def dijkstra(graph, start):
    """
    Perform Dijkstra's Algorithm to find the shortest paths from a source vertex
    to all other vertices in a weighted graph.

    Parameters:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      Each key is a vertex, and the value is a list of tuples (neighbor, weight).
        start (any): The starting vertex for the algorithm.

    Returns:
        dict: A dictionary where the keys are vertices and the values are the shortest
              distances from the start vertex to that vertex.
    """
    # Initialize distances with infinity and set the distance to the start vertex as 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Min-heap to store (distance, vertex)
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        # Skip if the current distance is not optimal
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path is found, update the distance and push to the heap
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }

    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")