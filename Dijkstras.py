def dijkstra(graph, source):
    dist = [float('inf')] * len(graph)
    dist[source] = 0

    pq = [(0, source)]
    while pq:
        d, u = findMin(pq)
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                pq.append((dist[v], v))

    return dist

def findMin(queue):
    min_vertex = queue[0]
    for vertex in queue:
        if(vertex[0] < min_vertex[0]):
            min_vertex = vertex
    
    queue.remove(min_vertex)
    return min_vertex

num = int(input("Enter the number of edges: "))
graph = {}
for i in range(num):
    u, v, w = input("Enter the (source, destination, weight): ").split()
    if int(u) not in graph:
        graph[int(u)] = []
    if int(v) not in graph:
        graph[int(v)] = []
    
    graph[int(u)].append((int(v), int(w)))
    graph[int(v)].append((int(u), int(w)))

source = int(input("Enter the source vertex: "))
print("Shortest distances from the source vertex: ", dijkstra(graph, source))