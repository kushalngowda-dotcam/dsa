def dfs(graph,start,visited=None,order= None):
    if visited is None:
        visited=set()
    if order is None:
        order=[]
    visited.add(start)
    order.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph,n,visited,order)
    return order
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }
    start = 1
    result = dfs(graph, start)
    print("DFS Traversal:", result)