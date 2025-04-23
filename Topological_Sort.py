from collections import deque, defaultdict

def kahn_topological_sort(adj):
    """
    Kahn’s algorithm for topological sorting.
    adj: dict mapping each node to a list of its neighbors.
    Returns a list in topologically sorted order, or raises ValueError if a cycle is detected.
    """
    # 1. Compute in-degrees
    in_deg = defaultdict(int)
    for u in adj:
        in_deg[u]  # ensure u in in_deg
        for v in adj[u]:
            in_deg[v] += 1

    # 2. Initialize queue with all 0 in-degree nodes
    q = deque([u for u, d in in_deg.items() if d == 0])
    topo_order = []

    # 3. Process
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)

    # 4. Check for cycle
    if len(topo_order) != len(in_deg):
        raise ValueError("Graph has at least one cycle")
    return topo_order


def dfs_topological_sort(adj):
    """
    DFS-based topological sort.
    adj: dict mapping each node to a list of its neighbors.
    Returns a list in topologically sorted order, or raises ValueError if a cycle is detected.
    """
    visited = set()
    temp_mark = set()
    stack = []

    def visit(u):
        if u in temp_mark:
            raise ValueError(f"Cycle detected at node {u}")
        if u not in visited:
            temp_mark.add(u)
            for v in adj.get(u, []):
                visit(v)
            temp_mark.remove(u)
            visited.add(u)
            stack.append(u)

    for node in adj:
        if node not in visited:
            visit(node)

    # reverse to get correct order
    return stack[::-1]


if __name__ == "__main__":
    # Example DAG
    graph = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }

    print("Kahn’s order:", kahn_topological_sort(graph))
    print("DFS order:  ", dfs_topological_sort(graph))
