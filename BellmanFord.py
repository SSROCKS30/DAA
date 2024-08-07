def bellmanFord(edges, V, source):
    dist = [float('inf')] * V
    dist[source] = 0

    for i in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return "Graph contains negative weight cycle"
        
    return dist

V = int(input('Enter the number of vertices: '))
E = int(input('Enter the number of edges: '))
edges = []
for i in range(E):
    u, v, w = map(int, input('Enter the (source, destination, weight): ').split())
    edges.append((u, v, w))

source = int(input('Enter the source vertex: '))
print(bellmanFord(edges, V, source))