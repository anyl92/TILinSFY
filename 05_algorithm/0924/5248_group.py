import sys
sys.stdin = open('input.txt', 'r')

def find(i):
    if V[i] == 0:
        V[i] = cnt
    for j in range(1, N+1):
        if L[i][j] == 1 and V[j] == 0:
            find(j)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    G = list(map(int, input().split()))
    L = [[0] * (N+1) for _ in range(N+1)]

    while G:
        a = G.pop(0)
        b = G.pop(0)
        L[a][b] = 1
        L[b][a] = 1

    V = [0] * (N+1)
    cnt = 1
    for i in range(1, N+1):
        find(i)
        cnt += 1

    print('#%d %d' % (tc, len(set(V))-1))