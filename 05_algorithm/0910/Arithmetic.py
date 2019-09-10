import sys
sys.stdin = open('input.txt', 'r')

def inorder(T):
    if tree[T][1] + tree[T][2] == 0:
        return tree[T][0]
    if tree[T][0] == '+':
        return inorder(tree[T][1]) + inorder(tree[T][2])
    if tree[T][0] == '-':
        return inorder(tree[T][1]) - inorder(tree[T][2])
    if tree[T][0] == '*':
        return inorder(tree[T][1]) * inorder(tree[T][2])
    if tree[T][0] == '/':
        return inorder(tree[T][1]) / inorder(tree[T][2])

for tc in range(10):
    N = int(input())
    result = ''
    tree = [[0, 0, 0] for _ in range(N+1)]

    for i in range(N):
        temp = list(map(str, input().split()))
        if len(temp) > 2:
            tree[int(temp[0])][0] = temp[1]
            tree[int(temp[0])][1] = int(temp[2])
            tree[int(temp[0])][2] = int(temp[3])
        else:
            tree[int(temp[0])][0] = int(temp[1])

    print('#%d %d' % (tc+1, inorder(1)))

