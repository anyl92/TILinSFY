import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    L = sorted(L, key=lambda x:x[1])

    res = []
    cnt = 0
    for k in range(len(L)):
        i, tmp = 0, 1
        while i < len(L):
            for j in range(1+i, len(L)):
                if L[i][1] <= L[j][0]:
                    i = j
                    tmp += 1
                    continue
                else:
                    pass
            i += 1
            if cnt < tmp:
                cnt = tmp
    print('#%d %d' % (tc, cnt))