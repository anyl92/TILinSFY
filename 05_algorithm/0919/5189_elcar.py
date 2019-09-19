import sys
sys.stdin = open('input.txt', 'r')

def perm(k, T):
    global minn

    if k == M:
        T = [0] + T + [0]
        el = 0
        for i in range(N):
            el += L[T[i]][T[i+1]]
        if el < minn:
            minn = el
    else:
        for i in range(k, M):
            T[k], T[i] = T[i], T[k]
            perm(k+1, T)
            T[k], T[i] = T[i], T[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    T = [i for i in range(1, N)]
    M = len(T)
    minn = 9999999

    perm(0, T)
    print('#%d %d' % (tc, minn))
