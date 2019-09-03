import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = [list(input()) for _ in range(5)]

    li = []
    i, j = 0, 0

    comp = []
    for k in L:
        comp += [len(k)]

    while j < max(comp):  # 열
        while i < len(L):  # 행
            if j > len(L[i])-1:
                i += 1
                continue
            li += [L[i][j]]
            i += 1
        i = 0
        j += 1
    print('#%d %s' % (tc, ''.join(li)))