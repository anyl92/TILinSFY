import sys
sys.stdin = open('input.txt', 'r')

def preorder(n):
    global count
    if n:
        for i in range(len(tree[n])):
            preorder(tree[n][i])
            count += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    count = 0

    tree = [[] for _ in range(E*2)]
    for i in range(len(temp)//2):
        tree[temp[2*i]].append(temp[2*i+1])
    preorder(N)

    if N in temp:
        print('#%d %d' % (tc, count+1))
    else:
        print('#%d %d' % (tc, 0))