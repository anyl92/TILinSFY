import sys
sys.stdin = open('input.txt', 'r')

def calc(p, q):
    resp = p[0] + q[0]
    resq = p[1] + q[1]

    for i in range(1, len(l), 3):
        if l[i] == resp:
            if l[i + 1] == resq:
                return l[i - 1]

T = int(input())
L = [list(map(int, input().split())) for tc in range(T)]

k = 1
n = 1
l = []
while n < 50001:
    x = 1
    y = k
    for _ in range(k):
        l += [n, x, y]
        x += 1
        y -= 1
        n += 1
        if n == 50001:
            break
    k += 1

tc = 1
p, q = [], []
for i in L:
    if i[0] == l[(i[0]-1)*3]:
        p += [l[(i[0]-1)*3 + 1], l[(i[0]-1)*3 + 2]]
    if i[1] == l[(i[1]-1)*3]:
        q += [l[(i[1]-1)*3 + 1], l[(i[1]-1)*3 + 2]]
    print('#%d %d' % (tc, calc(p, q)))
    tc += 1
    p, q = [], []