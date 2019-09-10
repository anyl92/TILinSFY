import sys
sys.stdin = open('input.txt', 'r')

def change(t):
    if t < 1:
        return
    elif tree[t//2] > tree[t]:
        tree[t//2], tree[t] = tree[t], tree[t//2]
        change(t//2)

def heap(t):
    if t > N:
        return
    new.append(tree[t])
    change(t)
    heap(t+1)

def find(tree):
    res = 0
    n = tree.index(tree[-1])
    while n > 0:
        n //= 2
        res += tree[n]
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    tree = [0] + L
    new = [0]

    heap(1)
    print('#%d %d' % (tc, find(tree)))
