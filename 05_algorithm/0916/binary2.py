import sys
sys.stdin = open('input.txt', 'r')

def func(M):
    res = []
    while M-int(M) != 0:
        M = (M-int(M)) * 2
        if int(M) == 1:
            res += ['1']
            M -= 1
        elif int(M) == 0:
            res += ['0']
        if len(res) >= 13:
            return print('#%d' % tc, 'overflow')
    return print('#%d %s' % (tc, ''.join(res)))

T = int(input())
for tc in range(1, T+1):
    M = float(input())
    func(M)