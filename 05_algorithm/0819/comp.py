#4864

import sys
sys.stdin = open('comp_input.txt')

T = int(input())
for tc in range(1, T+1):
    C = str(input())
    M = str(input())

    lc = len(C)
    if C in M:
        res = 1
        print('#%d %d' % (tc, res))
    else:
        res = 0
        print('#%d %d' % (tc, res))
