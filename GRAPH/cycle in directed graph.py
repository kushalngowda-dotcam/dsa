def directedcyl(graph):
    visited=set()
    resta=set()
    def dfs(node):
        if node in resta:
            return True
        if node in visited:
            return False
        visited.add(node)
        resta.add(node)
        for n in graph[node]:
            if dfs(n):
                return True
        resta.remove(node)
        return False
    for node in graph:
        if dfs(node):
            return True
    return  False
if __name__ == "__main__":
    graph1 = {
        0: [1],
        1: [2],
        2: [0],   # cycle: 0 → 1 → 2 → 0
        3: []
    }
    graph2 = {
        0: [1],
        1: [2],
        2: [],
        3: []
    }

    print("Graph1 has cycle?", directedcyl(graph1))  # True
    print("Graph2 has cycle?", directedcyl(graph2))  # False

