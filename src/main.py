import inquirer
from design_paradigms.greedy_algorithms.activity_selection import activity_selection
from design_paradigms.greedy_algorithms.fractional_knapsack import fractional_knapsack, Item
from design_paradigms.greedy_algorithms.huffman_coding import huffman_coding
from design_paradigms.greedy_algorithms.kruskals_algorithm import kruskals_algorithm
from design_paradigms.greedy_algorithms.prims_algorithm import prims_algorithm
from graph_algorithms.dijkstras_algorithm import dijkstra
from design_paradigms.divide_and_conquer.quick_sort import quick_sort
from design_paradigms.divide_and_conquer.merge_sort import merge_sort
from design_paradigms.dynamic_programming.floyd_warshall import floyd_warshall

def run_activity_selection():
    print("Running Activity Selection...")
    start_times = list(map(int, input("Enter start times (space-separated): ").split()))
    finish_times = list(map(int, input("Enter finish times (space-separated): ").split()))
    result = activity_selection(start_times, finish_times)
    print(f"Selected activities: {result}")

def run_fractional_knapsack():
    print("Running Fractional Knapsack...")
    n = int(input("Enter the number of items: "))
    items = []
    for i in range(n):
        value, weight = map(int, input(f"Enter value and weight for item {i + 1} (space-separated): ").split())
        items.append(Item(value, weight))
    capacity = int(input("Enter the capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in the knapsack: {max_value}")

def run_huffman_coding():
    print("Running Huffman Coding...")
    data = input("Enter the string to encode: ")
    codes, encoded_data = huffman_coding(data)
    print("Huffman Codes:", codes)
    print("Encoded Data:", encoded_data)

def run_kruskals_algorithm():
    print("Running Kruskal's Algorithm...")
    vertices = input("Enter vertices (space-separated): ").split()
    edges = []
    m = int(input("Enter the number of edges: "))
    for _ in range(m):
        u, v, weight = input("Enter edge (u v weight): ").split()
        edges.append((u, v, int(weight)))
    mst = kruskals_algorithm(vertices, edges)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

def run_prims_algorithm():
    print("Running Prim's Algorithm...")
    graph = {}
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Enter vertex: ")
        neighbors = input(f"Enter neighbors of {vertex} as (neighbor weight) pairs (space-separated): ").split()
        graph[vertex] = [(neighbors[i], int(neighbors[i + 1])) for i in range(0, len(neighbors), 2)]
    start_vertex = input("Enter the starting vertex: ")
    mst = prims_algorithm(graph, start_vertex)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

def run_dijkstra():
    print("Running Dijkstra's Algorithm...")
    graph = {}
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Enter vertex: ")
        neighbors = input(f"Enter neighbors of {vertex} as (neighbor weight) pairs (space-separated): ").split()
        graph[vertex] = [(neighbors[i], int(neighbors[i + 1])) for i in range(0, len(neighbors), 2)]
    start_vertex = input("Enter the starting vertex: ")
    shortest_paths = dijkstra(graph, start_vertex)
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")

def run_merge_sort():
    print("Running Merge Sort...")
    arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

def run_quick_sort():
    print("Running Quick Sort...")
    arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
    print("Original array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)

def run_floyd_warshall():
    print("Running Floyd-Warshall Algorithm...")
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix row by row (use 'inf' for infinity):")
    graph = []
    for _ in range(n):
        row = input().split()
        graph.append([float('inf') if x == 'inf' else int(x) for x in row])
    result = floyd_warshall(graph)
    print("Shortest distances between every pair of vertices:")
    for row in result:
        print(row)
def run_depth_first_search():
    print("Running Depth First Search...")
    graph = {}
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Enter vertex: ")
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
        graph[vertex] = neighbors
    start_vertex = input("Enter the starting vertex: ")

    visited = set()

    def dfs(vertex):
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                dfs(neighbor)

    print("DFS Traversal:")
    dfs(start_vertex)
    print()


def run_breadth_first_search():
    print("Running Breadth First Search...")
    graph = {}
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Enter vertex: ")
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").split()
        graph[vertex] = neighbors
    start_vertex = input("Enter the starting vertex: ")

    visited = set()
    queue = [start_vertex]

    print("BFS Traversal:")
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph.get(vertex, []))
    print()


def main():
    questions = [
        inquirer.List(
            "algorithm",
            message="Choose an algorithm to run:",
            choices=[
                "Activity Selection", "Fractional Knapsack", "Huffman Coding",
                "Kruskal's Algorithm", "Prim's Algorithm", "Dijkstra's Algorithm",
                "Merge Sort", "Quick Sort", "Floyd-Warshall Algorithm", "Depth First Search", "Breadth First Search"
            ],
        )
    ]
    answers = inquirer.prompt(questions)

    if answers["algorithm"] == "Activity Selection":
        run_activity_selection()
    elif answers["algorithm"] == "Fractional Knapsack":
        run_fractional_knapsack()
    elif answers["algorithm"] == "Huffman Coding":
        run_huffman_coding()
    elif answers["algorithm"] == "Kruskal's Algorithm":
        run_kruskals_algorithm()
    elif answers["algorithm"] == "Prim's Algorithm":
        run_prims_algorithm()
    elif answers["algorithm"] == "Dijkstra's Algorithm":
        run_dijkstra()
    elif answers["algorithm"] == "Merge Sort":
        run_merge_sort()
    elif answers["algorithm"] == "Quick Sort":
        run_quick_sort()
    elif answers["algorithm"] == "Floyd-Warshall Algorithm":
        run_floyd_warshall()
    elif answers["algorithm"] == "Depth First Search":
        run_depth_first_search()
    elif answers["algorithm"] == "Breadth First Search":
        run_breadth_first_search()
    


if __name__ == "__main__":
    main()