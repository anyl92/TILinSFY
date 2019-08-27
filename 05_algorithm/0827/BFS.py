# def BFS(G, v):
#     visited = [0]*n
#     queue= []
#     queue.append(v)
#     while queue:
#         t = queue.pop(0)
#         if not visited[t]:
#             visited[t] = True
#             visit(t)
#         for i in G[t]:
#             if not visited[i]:
#                 queue.append(i)
#324
L = []
Q = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
R = []
for i in range(len(Q)):
    R[i] = Q[i]

for i in range(0, len(Q)-1, 2):
    L.append([Q[i], Q[i+1]])
print(L) #[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]
#v = L[0][0]



q = [0]*10
visited = [0]*8

def BFS(L, v):
    f = r = -1
    r += 1
    q[r] = w

    print('%d'%q[r])
    visited[w] = 1

    while f != r:
        f += 1
        w = q[f]
        for i in range(3):
            if G[w][i] and not visited[G[w][i]]:
                r += 1
                q[r]= G[w][i]
                print('%d'%q[r])



#     visited = [0]*7
#     visited.append(L[0][0])
#
#     queue = []
#     queue.append(L[0][0])
#
#     while queue:
#         t = queue.pop(0)
#         if not visited[t]:
#             visited[t] = True
#
#
#
# BFS(L,v)
    # while queue:
    #     t = queue.pop(0)
    #     if not visited[t]:
    #         visited[t] = True