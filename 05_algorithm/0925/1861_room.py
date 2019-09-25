import sys
sys.stdin = open('input.txt', 'r')

def BFS(y, x):
    global path, max_cnt

    V[y][x] = 1
    q = [[y, x]]
    cnt = 1

    i = x
    j = y

    while q:
        for _ in range(len(q)):
            c = q.pop(0)
            for d in dir:
                y = c[0]
                x = c[1]
                idy = c[0] + d[0]
                idx = c[1] + d[1]
                if 0 <= idy < N and 0 <= idx < N:

                    if (L[y][x])+1 == L[idy][idx]:
                        q.append([idy, idx])
                        V[idy][idx] = 1
                        cnt += 1
    if cnt >= max_cnt:
        max_cnt = cnt
        # print(max_cnt)
        path += [L[j][i]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    V = [[0] * N for _ in range(N)]
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    max_cnt = 0
    path = []

    for y in range(N):
        for x in range(N):
            BFS(y, x)

    print('#%d %d %d' % (tc, min(path), max_cnt))