def DFS(graph, source):
    visited = []
    dfs = []
    def dfsRecursive(vertex):
        dfs.append(vertex)
        visited.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfsRecursive(neighbour)

    dfsRecursive(source)
    return dfs

num = int(input("Enter the number of edges: "))
graph = {}
for i in range(num):
    u, v = map(int, input("Enter the (source, destination): ").split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

source = int(input("Enter the source vertex: "))
print("DFS: ", DFS(graph, source))