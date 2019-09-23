A = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
print(A)

G = [[] for _ in range(8)]
for i in range(len(A)//2):
    G[A[2 * i]].append(A[2 * i + 1])
    G[A[2 * i + 1]].append(A[2 * i])
print(G)

def DFS(G, start):
    v = []
    s = [start]

    while s:
        n = s.pop()
        if n not in v:
            v.append(n)
            s.extend(G[n])
    return v

print(DFS(G, 1))


# def dfs_visit(adj, u, V):
#     V.append(u)
#     for v in adj[u]:
#         if v not in V:
#             dfs_visit(adj, v, V)
#
# def dfs(adj, s):
#     V = []
#     dfs_visit(adj, s, V)
#     return V
#
# print(dfs(G, 1))


v = []

def dfs(G, start, v):
    v.append(start)
    for i in G[start]:
        if i not in v:
            dfs(G, i, v)
    return v

print(dfs(G, 1, v))