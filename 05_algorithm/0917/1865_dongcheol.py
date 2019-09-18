import sys
sys.stdin = open('input.txt', 'r')

def perm(k, s):
    global Max
    if s <= Max:
        return

    if k == N:
        tsum = 1
        for i in range(N):
            tsum *= L[i][t[i]] / 100
        if tsum > Max:
            Max = tsum
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = i
            visited[i] = 1
            perm(1+k, s*L[k][i]/100)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    Max = 0
    t = [0] * N
    visited = [0] * N
    perm(0, 1)
    print('#%d %.6f' % (tc, Max*100))