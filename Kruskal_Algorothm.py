class DisjointSet:
    """Disjoint Set Union (Union–Find) with path compression and union by rank."""
    def __init__(self, n):
        # parent[i] = parent of i; initially itself
        self.parent = list(range(n))
        # rank[i] = approximate tree depth for balancing
        self.rank = [0] * n

    def find(self, x):
        """Find the representative of the set containing x, with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y. Returns True if merged, False if already in same set."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # already connected

        # attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskal(n_vertices, edges):
    """
    Kruskal's algorithm to compute the Minimum Spanning Tree (MST).

    Args:
        n_vertices (int): Number of vertices, labeled 0 to n_vertices-1.
        edges (List[Tuple[int, int, float]]): List of edges (u, v, weight).

    Returns:
        mst_edges (List[Tuple[int, int, float]]): Edges included in the MST.
        total_weight (float): Sum of the weights of the MST edges.
    """
    # Sort edges by increasing weight
    edges_sorted = sorted(edges, key=lambda e: e[2])
    
    dsu = DisjointSet(n_vertices)
    mst_edges = []
    total_weight = 0.0

    for u, v, w in edges_sorted:
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            # Stop if we've added n_vertices-1 edges
            if len(mst_edges) == n_vertices - 1:
                break

    return mst_edges, total_weight


if __name__ == "__main__":
    # Example usage:
    # Graph with 4 vertices (0,1,2,3) and weighted edges
    example_edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    n = 4

    mst, weight = kruskal(n, example_edges)
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"  {u} -- {v}  (weight {w})")
    print(f"Total weight of MST: {weight}")
