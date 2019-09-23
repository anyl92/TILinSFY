A = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
print(A)

G = [[] for _ in range(len(A)//2)]
for i in range(len(A)//2):
    G[A[2*i]].append(A[2*i+1])
    G[A[2*i+1]].append(A[2*i])
print(G)

def BFS(G, start):
    v = []
    q = [start]

    while q:
        n = q.pop(0)
        if n not in v:
            v.append(n)
            q.extend(G[n])
    return v

print(BFS(G, 1))