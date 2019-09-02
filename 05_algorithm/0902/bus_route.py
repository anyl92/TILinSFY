import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    L = [int(input()) for _ in range(P)]
    print(N, M, P, L)

    counting = [0] * 5005

    for i in range(len(M)):
        for j in range(M[i][0], M[i][1]+1):
            counting[j] += 1
    print(counting)

    res = ''
    for i in L:
        res += str(counting[i]) + ' '

    print('#%d %s' % (tc, res))