import sys
sys.stdin = open('input.txt', 'r')

def check(L):
    for i in range(9):
        if len(set(L[i])) == 9:
            continue
        else:
            return False

    for i in range(9):
        sero = []
        for j in range(9):
            sero += [L[j][i]]

            if i % 3 == 0 and j % 3 == 0:
                squa = []
                for k in range(3):
                    for l in range(3):
                        squa += [L[i+k][j+l]]
            if len(set(squa)) == 9:
                continue
            else:
                return False

        if len(set(sero)) == 9:
            continue
        else:
            return False

    return True

T = int(input())
for tc in range(1, T+1):
    L = [list(map(int, input().split())) for _ in range(9)]

    if check(L):
        print('#%d' % tc, 1)
    else:
        print('#%d' % tc, 0)

