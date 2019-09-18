import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    L = list(map(str, range(10)))
    H = []
    R = []

    for i in M:
        if i not in L:
            tmp = ord(i)-ord('A')+10
        else:
            tmp = int(i)
        H += [tmp]

    for i in H:
        B = []
        j = 0
        while j < 4:
            B += [i % 2]
            i //= 2
            j += 1
        B.reverse()
        R += B
    R = list(map(str, R))
    print('#%d' % tc, ''.join(R))