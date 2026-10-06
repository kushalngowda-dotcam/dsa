from collections import deque
def bfs(graph,start):
    visited=set()
    order=[]
    queue=deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        order.append(node)
        for neighbors in graph[node]:
            if neighbors not in visited:
                visited.add(neighbors)
                queue.append(neighbors)
    return order
# Example usage
if __name__ == "__main__":
    # Graph represented as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }
    start = 1
    result = bfs(graph, start)
    print("BFS Traversal:", result)