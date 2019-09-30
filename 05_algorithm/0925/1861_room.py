import sys
sys.stdin = open('input.txt', 'r')

def BFS(y, x, L, V):
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = [[y, x]]
    path = []

    while q:
        c = q.pop(0)
        y, x = c[0], c[1]
        if not V[y][x]:
            path.append(L[y][x])
            V[y][x] = 1

        for d in dir:
            idy, idx = c[0] + d[0], c[1] + d[1]
            if 0 <= idy < N and 0 <= idx < N and not V[idy][idx]:
                if abs(L[y][x] - L[idy][idx]) == 1:
                    q.append([idy, idx])
    return [len(path), min(path)]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    max_move = 0
    min_cnt = N

    for y in range(N):
        for x in range(N):
            if not V[y][x]:
                move, cnt = BFS(y, x, L, V)
                if move > max_move:
                    max_move = move
                    min_cnt = cnt
                elif move == max_move and min_cnt > cnt:
                    min_cnt = cnt
    print('#%d %d %d' % (tc, min_cnt, max_move))