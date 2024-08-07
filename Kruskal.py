def findParent(parent, i):
    if parent[i] == i:
        return i
    return findParent(parent, parent[i])

def union(parent, rank, x, y):
    xroot = findParent(parent, x)
    yroot = findParent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(V, edges):
    parent = []
    rank = []

    edges.sort(key=lambda x: x[2])  

    for node in range(V):
        parent.append(node)
        rank.append(0)

    mst_cost = 0
    mst_edges = []

    for u, v, wt in edges:
        x = findParent(parent, u)
        y = findParent(parent, v)

        if x != y:
            mst_cost += wt
            mst_edges.append((u, v, wt))
            union(parent, rank, x, y)

    return mst_cost, mst_edges

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

edges = []
for i in range(E):
    u, v, w = input("Enter the (source, destination, weight): ").split()
    edges.append((int(u), int(v), int(w)))

mst_cost, mst_edges = kruskal(V, edges)
print("MST Cost: ", mst_cost)
print("MST Edges: ", mst_edges)