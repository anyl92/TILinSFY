import sys
sys.stdin = open('input.txt', 'r')

def runn(C):
    for i in range(2, len(C)):
        if C[i] and C[i-1] and C[i-2]:
            return True

def tri(C):
    for i in C:
        if i >= 3:
            return True

T = int(input())
for tc in range(1, T+1):
    L = list(map(int, input().split()))

    C1 = [0] * 10
    C2 = [0] * 10
    res = 0

    for i in range(len(L)):
        if i % 2 == 0:
            C1[L[i]] += 1
            if i > 4:
                if runn(C1) or tri(C1):
                    res = 1
                    break
        else:
            C2[L[i]] += 1
            if i > 5:
                if runn(C2) or tri(C2):
                    res = 2
                    break

    print('#%d %d' % (tc, res))