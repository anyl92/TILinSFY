import sys
sys.stdin = open('rabbit_input.txt', 'r')

def checking(L, i, j, y_cnt):
    cnt, x_cnt = 0, 0
    x, y = i, j

    while L[y][x] != 0:
        L[y][x] = 0
        x += dx[3]
        cnt += 1
    x -= cnt
    x_cnt = cnt
    y += dy[1]
    if L[y][x] != 0:
        cnt = 0
        y_cnt += 1
        return checking(L, x, y, y_cnt)
    elif L[y][x] == 0:
        y_cnt += 1
        return [y_cnt, x_cnt]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    x, y, cnt, y_cnt = 0, 0, 0, 0

    arr = []
    while y < N:
        while x < N:
            while L[y][x] != 0:
                arr.append(checking(L, x, y, y_cnt))
            x += 1
        y += 1
        x = 0

    comp_list = [0] * len(arr)
    for i in range(len(arr)):
        comp_list[i] = arr[i][0] * arr[i][1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if comp_list[i] > comp_list[j]:
                comp_list[i], comp_list[j] = comp_list[j], comp_list[i]
                arr[i], arr[j] = arr[j], arr[i]
            elif comp_list[i] == comp_list[j]:
                if arr[i][0] > arr[j][0]:
                    arr[i], arr[j] = arr[j], arr[i]

    res = ''
    for i in range(len(arr)):
        for j in range(2):
            res += str(arr[i][j]) + ' '
    print('#%d %d %s' % (tc, len(arr), res))