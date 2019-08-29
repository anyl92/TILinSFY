import sys
sys.stdin = open('rabbit_input.txt', 'r')
L = [list(map(int, input().split())) for _ in range(10)]

def kill(L, a, b):
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    count = 0
    for k in range(8):
        x, y = a, b
        while L[y][x] != 2 and 0<=x+dx[k]<10 and 0<=y+dy[k]<10:
            x += dx[k]
            y += dy[k]
            if L[y][x] == 1:
                L[y][x] = -1
                count += 1
    return count
res = 0
for y in range(10):
    for x in range(10):
        if L[y][x] == 3:
            res += kill(L,x,y)
print(res)