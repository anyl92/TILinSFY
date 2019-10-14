import sys
sys.stdin = open('17070.txt', 'r')

def is_wall(x, y, status):
    if x < 0 or y < 0 or x >= N or y >= N or house[x][y] == 1:
        return False
    elif status == 3 and (house[x-1][y] == 1 or house[x][y-1] == 1):
        return False
    else:
        return True

def find_root(house, x, y, status):
    global count

    if (x, y) == (N-1, N-1):
        count += 1
    elif status == 1:
        next_x, next_y = x, y + 1
        if is_wall(next_x, next_y, 1):
            find_root(house, next_x, next_y, 1)
        next_x, next_y = x + 1, y + 1
        if is_wall(next_x, next_y, 3):
            find_root(house, next_x, next_y, 3)
    elif status == 2:
        next_x, next_y = x + 1, y
        if is_wall(next_x, next_y, 2):
            find_root(house, next_x, next_y, 2)
        next_x, next_y = x + 1, y + 1
        if is_wall(next_x, next_y, 3):
            find_root(house, next_x, next_y, 3)

    elif status == 3:
        next_x, next_y = x, y + 1
        if is_wall(next_x, next_y, 1):
            find_root(house, next_x, next_y, 1)
        next_x, next_y = x + 1, y
        if is_wall(next_x, next_y, 2):
            find_root(house, next_x, next_y, 2)
        next_x, next_y = x + 1, y + 1
        if is_wall(next_x, next_y, 3):
            find_root(house, next_x, next_y, 3)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
status = 1    # 1: 가로, 2: 세로, 3: 대각선
start_x, start_y = 0, 1
count = 0

find_root(house, start_x, start_y, status)

print(count)