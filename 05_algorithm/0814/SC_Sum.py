import sys
sys.stdin = open('SC_input.txt', 'r')

def rowsum(arr):
    rowsum = 0
    rowsum1 = 0
    rowsum2 = [0] * 100
    for x in range(100):
        for y in range(100):
            rowsum1 += arr[x][y]
        rowsum2[x] = rowsum1
        rowsum1 = 0
    for i in range(len(rowsum2)):
        if rowsum < rowsum2[i]:
            rowsum = rowsum2[i]
    return rowsum

def colsum(arr):
    colsum = 0
    colsum1 = 0
    colsum2 = [0] * 100
    for y in range(100):
        for x in range(100):
            colsum1 += arr[x][y]
        colsum2[y] = colsum1
        colsum1 = 0
    for i in range(len(colsum2)):
        if colsum < colsum2[i]:
            colsum = colsum2[i]
    return colsum

def revslash(arr):
    revslash = 0
    y = 0
    while y < 100:
        revslash += arr[y][y]
        y += 1
    return revslash

def slash(arr):
    slash = 0
    x = 99
    y = 0
    while y < 100:
        slash += arr[x][y]
        x -= 1
        y += 1
    return slash

for i in range(10):
    li = []
    T = int(input())
    for tc in range(100):
        li1 = list(map(int, input().split()))
        li.append(li1)

    r = rowsum(li)
    c = colsum(li)
    rs = revslash(li)
    s = slash(li)

    max_check_list = [r, c, rs, s]
    max_check = r
    for j in range(len(max_check_list)):
        if max_check < max_check_list[j]:
            max_check = max_check_list[j]
        r = max_check
    res = '#%d %d' % (i + 1, max_check)
    print(res)