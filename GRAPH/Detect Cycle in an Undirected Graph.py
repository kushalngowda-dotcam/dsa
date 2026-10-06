def find_cyc(graph):
    visited=set()
    def dfs(node,parent):
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                if dfs(n,node):
                    return True
            elif n !=parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node,-1):
                return True
    return False
if __name__ == "__main__":
    graph1 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]   # cycle: 0 → 1 → 2 → 3 → 0
    }
    graph2 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }

    print("Graph1 has cycle?", find_cyc(graph1))  # True
    print("Graph2 has cycle?", find_cyc(graph2))

