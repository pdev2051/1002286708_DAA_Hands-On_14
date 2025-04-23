from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # adjacency list: node -> list of neighbors
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an edge from u to v (for undirected graphs, also add v->u)."""
        self.adj[u].append(v)
        # Uncomment the next line if the graph is undirected:
        # self.adj[v].append(u)

    def dfs_recursive(self, start, visited=None):
        """
        Recursive DFS starting from `start`.
        Returns the list of nodes in the order they were visited.
        """
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]
        for neighbor in self.adj[start]:
            if neighbor not in visited:
                order.extend(self.dfs_recursive(neighbor, visited))
        return order

    def dfs_iterative(self, start):
        """
        Iterative DFS using an explicit stack.
        Returns the list of nodes in the order they were visited.
        """
        visited = set([start])
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            order.append(node)
            # Add neighbors to stack; reverse for similar order to recursive
            for neighbor in reversed(self.adj[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return order


if __name__ == "__main__":
    # Example usage:
    g = Graph()
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "D"), ("B", "E"),
        ("C", "F"), ("E", "F"),
        ("F", "G")
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Adjacency list:")
    for node, nbrs in g.adj.items():
        print(f"  {node}: {nbrs}")

    start_node = "A"
    print("\nDFS Recursive Order:", g.dfs_recursive(start_node))
    print("DFS Iterative Order:", g.dfs_iterative(start_node))
