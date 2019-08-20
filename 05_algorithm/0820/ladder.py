import sys
sys.stdin = open('ladder_input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    def findone(arr, i, j):  # arr, 99, ??
        while i != 0:
            if arr[i][j - 1]:
                while arr[i][j-1] == 1:
                    arr[i][j] = -1
                    j -= 1
            elif arr[i][j + 1]:
                while arr[i][j+1] == 1:
                    arr[i][j] = -1
                    j += 1
            else:
                arr[i][j] = -1
            i -= 1
        return j-1

    for j in range(1, 101):
        if arr[99][j] == 2:
            res = findone(arr, 99, j)
    print('#%d %d' % (tc, res))