def TSP(u,cost,minCost):
    if False not in visited: # All vertices are visited
        if adj[u][0]:   # If there is an edge from last vertex to first vertex
            cost += adj[u][0]
            minCost[0] = min(cost,minCost[0])
        return

    for v in range(V):
        if not visited[v] and adj[u][v]:   # If vertex v is not visited and there is an edge from u to v
            visited[v] = True
            TSP(v, cost+adj[u][v], minCost)
            visited[v] = False


V,E = map(int,input("Enter no. of vertices and edges : ").split())
adj = [[0]*V for _ in range(V)]
visited = [False]*V
for i in range(E):
    u,v,wt = map(int,input(f"Edge-{i+1} : ").split())
    adj[u][v] = adj[v][u] = wt

minCost = [float('inf')]
TSP(0,0,minCost)
print("minCost : ",minCost[0])

# Edge-1 : 0 1 2
# Edge-2 : 0 4 5
# Edge-3 : 0 3 12
# Edge-4 : 1 2 4
# Edge-5 : 1 3 8
# Edge-6 : 2 3 3
# Edge-7 : 2 4 3
# Edge-8 : 3 4 10