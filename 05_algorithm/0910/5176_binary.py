import sys
sys.stdin = open('input.txt', 'r')

def inorder(t):
    global count
    if tree[t]:
        inorder(2*t)
        count += 1
        temp = count
        cnt[t] = temp
        inorder(2*t+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [i for i in range(N+1)] + [0]*(N+1)
    cnt = [0 for _ in range(N*2)]
    count = 0

    inorder(1)
    print('#%d %d %d' % (tc, cnt[1], cnt[N//2]))