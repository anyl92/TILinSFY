import sys
sys.stdin = open('input.txt', 'r')

def quick(L, l, r):
    if l < r:
        s = partitionH(L, l, r)
        quick(L, l, s-1)
        quick(L, s+1, r)

def partitionH(L, l, r):
    p = l
    i = l
    j = r
    while i < j:
        while i < r and L[i] <= L[p]:
            i += 1
        while j > l and L[j] >= L[p]:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    L[p], L[j] = L[j], L[p]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    quick(L, 0, len(L)-1)
    print('#%d %d' % (tc, L[N//2]))