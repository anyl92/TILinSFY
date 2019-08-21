# 4865
import sys
sys.stdin = open('instring_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = str(input())
    L = str(input())

    count = 0
    max_count = 0
    res = ''
    for i in set(N):
        if i in L:
            for j in L:
                if i == j:
                    count += 1
                if count > max_count:
                    max_count = count
                    res = i
            count = 0
    print('#%d %d' % (tc, max_count))