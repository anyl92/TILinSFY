import sys
sys.stdin = open('input.txt', 'r')

def BFS(L, start):
    v = []
    q = [start]

    if L[1] != []:
        while q:
            n = q.pop(0)
            if n not in v:
                v.append(n)
                q.extend(L[n])
    return v

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    G = []
    for _ in range(M):
        G += list(map(int, input().split()))

    L = [[] for _ in range(len(G))]
    for i in range(len(G)//2):
        L[G[2 * i]].append(G[2 * i + 1])
        L[G[2 * i + 1]].append(G[2 * i])
    print(L)

    for i in range(2, len(L)):
        if i not in L[1]:
            L[i] = []
    print(L)

    R = BFS(L, 1)
    if 1 in R:
        R.pop(0)
    print('#%d %d' % (tc, len(R)))