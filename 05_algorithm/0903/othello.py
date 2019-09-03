import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(M)]

    arr = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N//2-1, N//2+1):
        for j in range(N//2-1, N//2+1):
            if i == j:
                arr[i][j] = 2
            else:
                arr[i][j] = 1

    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    for i in range(len(L)):
        x = L[i][0]-1
        y = L[i][1]-1
        arr[y][x] = L[i][2]

        for n in range(8):
            m = 1
            while 0 <= y+(dy[n]*m) < N and 0 <= x+(dx[n]*m) < N:
                if arr[y+(dy[n]*m)][x+(dx[n]*m)] == 0:
                    break
                if arr[y+(dy[n]*m)][x+(dx[n]*m)] == L[i][2]:
                    for k in range(1, m):
                        arr[y+(dy[n]*(m-k))][x+(dx[n]*(m-k))] = L[i][2]
                    break
                m += 1

    bl, wh = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                bl += 1
            elif arr[i][j] == 2:
                wh += 1

    print('#%d %d %d' % (tc, bl, wh))
