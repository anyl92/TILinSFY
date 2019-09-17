import sys
sys.stdin = open('input.txt', 'r')

def perm(k, s):
    global Max
    if s <= Max:
        return

    if k == N:
        tsum = 1
        for i in range(N):
            tsum *= arr[i][t[i]] / 100
        if tsum > Max:
            Max = tsum
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = i
            visited[i] = 1
            perm(k + 1, s * (arr[k][i] / 100))
            visited[i] = 0

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Max = 0
    t = [0]*N
    visited = [0]*N
    perm(0, 1)
    print('#%d %.6f' % (tc, Max*100))