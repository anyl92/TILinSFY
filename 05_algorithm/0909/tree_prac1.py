def preorder(n):
    if n:
        print(n, end=' ')
        preorder(tree[n][0])
        preorder(tree[n][1])


V = 13
tree = [[0]*2 for _ in range(V+1)]
temp = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

for i in range(len(temp)//2):
    parent, child = temp[i*2], temp[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

preorder(1)
print()
