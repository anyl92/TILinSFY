import sys
sys.stdin = open('bingo_input2.txt', 'r')
#1-20 2-12
def find_line(arr, i, j):
    line = 0
    x = 0
    y = 0
    check = 0
    while y < 5:
        if arr[i][y] == -1:  # 행
            if check == 4:
                line += 1
            else:
                check += 1
        y += 1

    check = 0
    while x < 5:
        if arr[x][j] == -1:  # 열
            if check == 4:
                line += 1
            else:
                check += 1
        x += 1

    if i == j:  # \대각선
        x = 0
        check = 0
        while x < 5:
            if arr[x][x] == -1:
                if check == 4:
                    line += 1
                else:
                    check += 1
            x += 1

    if i + j == 4:  # /대각선
        x = 0
        y = 4
        check = 0
        while x < 5:
            if arr[x][y] == -1:
                if check == 4:
                    line += 1
                else:
                    check += 1
            x += 1
            y -= 1
    return line

def find(arr, call):
    k = 0
    f = 0
    line = 0
    count = 0
    while k < 25:
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                if arr[i][j] == call[k]:
                    count += 1
                    arr[i][j] = -1
                    a, b = i, j
                    k += 1
                    j=-1
                    i=0
                    if count > 4:
                        line += find_line(arr, a, b)
                        if line >= 3:
                            return k
                j+=1
            i+=1

arr = [[char for char in map(int, input().split())] for i in range(5)]
call = []
for i in range(5):
    call += map(int, input().split())
print(find(arr, call))