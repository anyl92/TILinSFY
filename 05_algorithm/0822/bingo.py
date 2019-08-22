import sys
sys.stdin = open('bingo_input.txt', 'r')

arr = [[char for char in map(int, input().split())] for i in range(5)]
call = []
for i in range(5):
    call += map(int, input().split())


def find(arr, i, j):
    line = 0
    x = 0
    y = 0
    check = 0
    while y < 5:
        while arr[i][y] == -1:  # 행
            if check == 4:
                line += 1
                check = 0
            else:
                check += 1
                break
        y += 1

    check = 0
    while x < 5:
        while arr[x][j] == -1:  # 열
            if check == 4:
                line += 1
                check = 0
            else:
                check += 1
                break
        x += 1

    if i == j:  # \대각선
        x = y = 0
        check = 0
        while x < 5:
            while arr[x][y] == -1:
                if check == 4:
                    line += 1
                    check = 0
                else:
                    check += 1
                    break
            x += 1
            y += 1

    if i + j == 4:  # /대각선
        x = 0
        y = 4
        check = 0
        while x < 5:
            while arr[x][y] == -1:
                if check == 4:
                    line += 1
                    check = 0
                else:
                    check += 1
                    break
            x += 1
            y -= 1
    return line


k = 0
f = 0
flag = 1
line = 0
count = 0
while k < 26 and flag:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == call[k]:
                count += 1
                arr[i][j] = -1
                k += 1
                if count > 4:
                    line += find(arr, i, j)
                    if line == 3:
                        flag = 0
                        print(count)
                else:
                    f = 1
                    break
        if f:
            f = 0
            break
