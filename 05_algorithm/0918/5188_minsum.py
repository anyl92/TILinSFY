import sys
sys.stdin = open('input.txt', 'r')

def dfs(x, y, s):
    global min_sum, N

    if x == N-1 and y == N-1:
        if min_sum > s:
            min_sum = s

    if min_sum < s:
        return

    for i in range(2):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
            s += L[y + dy[i]][x + dx[i]]
            dfs(x+dx[i], y+dy[i], s)
            s -= L[y + dy[i]][x + dx[i]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1]
    dy = [1, 0]
    min_sum = 99999
    s = L[0][0]
    dfs(0, 0, s)
    print('#%d %d' % (tc, min_sum))