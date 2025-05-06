class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskals_algorithm(vertices, edges):
    """
    Kruskal's Algorithm to find the Minimum Spanning Tree (MST).

    Parameters:
        vertices (list): List of vertices in the graph.
        edges (list): List of edges in the graph, where each edge is represented as (u, v, weight).

    Returns:
        list: List of edges in the MST.
    """
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])

    disjoint_set = DisjointSet(vertices)
    mst = []

    for u, v, weight in edges:
        # Check if including this edge forms a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            disjoint_set.union(u, v)

    return mst

# Example usage
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 5),
        ('B', 'C', 4),
        ('B', 'D', 2),
        ('C', 'D', 6),
        ('D', 'E', 3)
    ]

    mst = kruskals_algorithm(vertices, edges)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")