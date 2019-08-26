import sys
sys.stdin = open('mag_input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]
    #print(L)

    count = 0
    for j in range(100):
        x = 0
        f = 0
        while x < 100:
            if f:
                if L[x][j] == 2:
                    count += 1
                    f = 0
            if L[x][j] == 1:
                f = 1
            x += 1
    print('#%d %d' % (tc, count))

