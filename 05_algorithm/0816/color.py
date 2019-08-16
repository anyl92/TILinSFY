# coding=utf-8
import sys
sys.stdin = open('color_input.txt', 'r')

count = 0
matrix = [[0 for _ in range(10)] for _ in range(10)]
matrix_reset = [[0 for _ in range(10)] for _ in range(10)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    for n in range(N):
        color_list = list(map(int, input().split()))
        for i in range(color_list[0], color_list[2]+1):
            for j in range(color_list[1], color_list[3]+1):
                matrix[i][j] += color_list[4]

    for x in range(10):
        for y in range(10):
            if matrix[x][y] == 3:
                count += 1

    matrix = [[0 for _ in range(10)] for _ in range(10)]
    print('#%d %d' % (tc, count))
    count = 0