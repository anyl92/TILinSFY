import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    k = 0

    while k < m:
        tmp = l[0]
        for i in range(1, n):
            l[i-1] = l[i]
        l[-1] = tmp
        k += 1

    print('#%d %d' % (tc, l[0]))