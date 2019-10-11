import sys
sys.stdin = open('17070.txt', 'r')


def func(r, c, d):
    global cnt
    dir = [[0, 1], [1, 0], [1, 1]]
    if d == dir[0]:
        dir[1] = False
    elif d == dir[1]:
        dir[0] = False

    for d in dir:
        if d:
            if 0 <= r+d[0] < N and 0 <= c+d[1] < N:
                rr = r + d[0]
                cc = c + d[1]
                if d == [1, 1]:
                    if L[r][c+1] == 1 or L[r+1][c] == 1:
                        return

                if L[rr][cc] == 0:
                    L[rr][cc] = 2
                    func(rr, cc, d)
                    L[rr][cc] = 0
                elif L[rr][cc] == 1:
                    continue
                elif L[rr][cc] == 3:
                    cnt += 1
                    return


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

L[0][1] = 2
L[N-1][N-1] = 3

cnt = 0
func(0, 1, [0, 1])
print(cnt)
