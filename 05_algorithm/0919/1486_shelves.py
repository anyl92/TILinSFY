import sys
sys.stdin = open('input.txt', 'r')

def powerset(L):
    global minn
    n = len(L)
    for i in range(1 << n):
        summ = 0
        for j in range(n+1):
            if i & (1 << j):
                summ += L[j]
                if summ >= B:
                    if summ < minn:
                        minn = summ

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    L = list(map(int, input().split()))
    minn = 9999999
    powerset(L)
    print('#%d %d' % (tc, minn-B))