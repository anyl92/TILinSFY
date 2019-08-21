import sys
sys.stdin = open('pel1_input.txt')

for tc in range(1, 11):
    N = int(input())
    L = [list(input()) for _ in range(8)]

    l = [0]*N
    count = 0
    for row in range(8):
        for j in range(8-N+1):
            for k in range(N):
                l[k] = L[row][k+j]
                if l == l[::-1]:
                    count += 1
            l = [0]*N

    for col in range(8):
        for i in range(8 - N + 1):
            for k in range(N):
                l[k] = L[k+i][col]
                if l == l[::-1]:
                    count += 1
            l = [0]*N

    print('#%d %d' % (tc, count))