import sys
sys.stdin = open('input.txt', 'r')

def inorder(T):
    global result
    if tree[T][1]:
        inorder(tree[T][1])
    result += tree[T][0]
    if tree[T][2]:
        inorder(tree[T][2])

for tc in range(10):
    N = int(input())
    result = ''
    tree = [[0, 0, 0] for _ in range(N+1)]

    for i in range(N):
        temp = list(map(str, input().split()))
        tree[int(temp[0])][0] = temp[1]
        if len(temp) > 2:
            tree[int(temp[0])][1] = int(temp[2])
        if len(temp) > 3:
            tree[int(temp[0])][2] = int(temp[3])

    inorder(1)
    print('#%d %s' % (tc+1, result))
