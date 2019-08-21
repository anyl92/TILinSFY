# 4861
import sys
sys.stdin = open('pel_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    L = [[char for char in input()] for _ in range(N)]
    #print(L)

    res = ''
    for row in L:
        for i in range(N-M+1):
            row_check = row[i:M+i+1]
            if row_check == row_check[::-1]:
                for k in row_check:
                    res += k + ' '
                print('#%s %s' % (tc, res))

    for col in range(len(L)):
        for l in range(N-M+1):
            col_check = [0] * M
            for j in range(M):
                col_check[j] = L[j+l][col]
            if col_check == col_check[::-1]:
                for k in col_check:
                    if col_check:
                        res += k + ' '
                print('#%s %s' % (tc, res))