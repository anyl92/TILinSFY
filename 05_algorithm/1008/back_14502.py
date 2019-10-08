import sys
sys.stdin = open('14502_input.txt', 'r')

def virus_infact():
    q = []
    for i in range(virus_cnt):
        x, y = virus_pos[i]
        q.append((x, y))

        while q:
            x, y = q.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                xx = x + dx
                yy = y + dy
                if not (0 <= xx < N and 0 <= yy < M):
                    continue
                if mat[xx][yy] == 0:
                    mat[xx][yy] = 2
                    q.append((xx, yy))


def count_safe_area():
    global ans
    tans = sum(mat, []).count(0)
    if ans < tans:
        ans = tans


def solve(k):
    arr = []
    for i in range(safe_cnt - 2):
        arr.append(i)
        for j in range(i + 1, safe_cnt - 1):
            arr.append(j)
            for k in range(j + 1, safe_cnt):
                arr.append(k)

                for i in range(3):
                    x, y = safe_pos[arr[i]]
                    mat[x][y] = 1

                virus_infact()
                count_safe_area()

                for ii in range(N):
                    for jj in range(M):
                        mat[ii][jj] = copy_mat[ii][jj]

                arr.pop(-1)
            arr.pop(-1)
        arr.pop(-1)


N, M = map(int, input().split())

mat = [0] * N
for i in range(N):
    mat[i] = list(map(int, input().split()))

copy_mat = [[0] * M for i in range(N)]
virus_cnt = 0
virus_pos = [0] * 10
safe_cnt = 0
safe_pos = [0] * (N * M)
for i in range(N):
    for j in range(M):
        if mat[i][j] == 2:
            virus_pos[virus_cnt] = (i, j)
            virus_cnt += 1
        elif mat[i][j] == 0:
            safe_pos[safe_cnt] = (i, j)
            safe_cnt += 1
        copy_mat[i][j] = mat[i][j]

ans = 0
solve(0)
print(ans)
