# coding=utf-8
import sys
sys.stdin = open('screw_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N2 = list(map(int, input().split()))
    N3 = [[0 for _ in range(2)] for _ in range(N)]
    k = 0
    total = []
    for i in range(N):
        for j in range(2):
            N3[i][j] = N2[j+k]
        k += 2

    i = 0
    tmp = N3.pop(0)
    total = [tmp,]
    while True:
        if len(total) == N:
            break
        for i in range(len(N3)):
            if total[-1][-1] == N3[i][0]:
                tmp = [N3.pop(i)]
                total = total + tmp
                break
            elif total[0][0] == N3[i][1]:
                tmp = [N3.pop(i)]
                total = tmp + total
                break
    print('#%d' % (tc), end=' ')
    for i in total:
        print(i[0], i[1], end=' ')
    print()
