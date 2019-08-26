# 4875
import sys
sys.stdin = open('miro_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input())) for _ in range(N)]

    def wall(x):
        global N
        if x < 0 or x > N-1:
            return False
        return 1

    def dfs(i, j):
        global res
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for k in range(4):
            if wall(i+dy[k])==True and wall(j+dx[k])==True:
                if M[i+dy[k]][j+dx[k]] == 0:
                    M[i][j] = 1
                    dfs(i+dy[k], j+dx[k])
                elif M[i+dy[k]][j+dx[k]] == 3:
                    res = 1

    res = 0
    for i in range(N):
        for j in range(N):
            if M[i][j] == 2:
                dfs(i, j)
    print('#%d %d' % (tc, res))
