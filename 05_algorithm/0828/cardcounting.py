import sys
sys.stdin = open('card_input.txt', 'r')

def overlap(L):
    for i in range(len(L)):
        for j in range(1+i, len(L)):
            if L[i] == L[j]:
                return False
    return True

def counting(L, res):
    if not overlap(L):
        return 'ERROR'
    s = 0
    d = 0
    h = 0
    c = 0
    for i in range(len(L)):
        if L[i][0] == 'S':
            s += 1
        elif L[i][0] == 'D':
            d += 1
        elif L[i][0] == 'H':
            h += 1
        elif L[i][0] == 'C':
            c += 1
    res += str(13 - s) + ' '
    res += str(13 - d) + ' '
    res += str(13 - h) + ' '
    res += str(13 - c)
    return res

T = int(input())
for tc in range(1, T + 1):
    N = str(input())
    L = []
    for i in range(0, len(N), 3):
        L.append(N[i] + N[i + 1] + N[i + 2])
    res = ''
    print('#%d %s' % (tc, counting(L, res)))