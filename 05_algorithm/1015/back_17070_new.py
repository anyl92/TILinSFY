import sys
sys.stdin = open('17070.txt', 'r')

import time
start = time.time()

def func(r, c, d):
    global cnt
    # 0 -> 가로, 1 -> 세로, 2 -> 대각선
    if r == N-1 and c == N-1:
        cnt += 1
        return

    if d == 0:  # [0, 1] [1, 1]
        if c+1 < N and L[r][c+1] == 0:
            func(r, c+1, 0)
        if r+1 < N and c+1 < N and L[r+1][c] == L[r][c+1] == L[r+1][c+1] == 0:
            func(r+1, c+1, 2)

    elif d == 1:  # [1, 0] [1, 1]
        if r+1 < N and L[r+1][c] == 0:
            func(r+1, c, 1)
        if r+1 < N and c+1 < N and L[r+1][c] == L[r][c+1] == L[r+1][c+1] == 0:
            func(r+1, c+1, 2)

    elif d == 2:  # [0, 1] [1, 0] [1, 1]
        if c+1 < N and L[r][c+1] == 0:
            func(r, c+1, 0)
        if r+1 < N and L[r+1][c] == 0:
            func(r+1, c, 1)
        if r+1 < N and c+1 < N and L[r+1][c] == L[r][c+1] == L[r+1][c+1] == 0:
            func(r+1, c+1, 2)


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
func(0, 1, 0)
print(cnt)

print(time.time() - start)