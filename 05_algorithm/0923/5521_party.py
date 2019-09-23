import sys
sys.stdin = open('input.txt', 'r')

def DFS(G, v)
    visited[v] = 1
    for i in range():
        if visited[i] == 0:
            DFS(G, i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M, L)

    for i in L:
        if i[0] == 1:
