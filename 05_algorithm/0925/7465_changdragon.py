import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(M)]

    for i in range(len(L)):
        if L[i]:
            for j in range(len(L)):
                if i != j and L[j]:
                    for k in L[j]:
                        if k in L[i]:
                            L[i] += L[j]
                            L[i] = list(set(L[i]))
                            L[j] = []
                            break
    cnt = 0
    per = []
    for i in L:
        if i:
            cnt += 1
        per += i
    res = N - len(per) + cnt

    print('#%d %d' % (tc, res))