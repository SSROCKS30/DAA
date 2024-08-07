def BFS(graph, source):
    visited = []
    queue = []
    bfs = []

    queue.append(source)

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            bfs.append(vertex)
            visited.append(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    return bfs

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
print("BFS: ", BFS(graph, source))