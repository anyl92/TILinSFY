import sys
sys.stdin = open('input.txt', 'r')

def DFS(G, start, v):
    v.append(start)
    for i in range():
        if visited[i] == 0:
            DFS(G, i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(M)]
    print(L)

    v = []