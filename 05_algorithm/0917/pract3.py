arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
res = 0
for i in range(0, (1<<n)):
    li = []
    res = 0
    for j in range(0, n):
        if i & (1<<j):
            li += [arr[j]]
            res += arr[j]
    if res == 0:
        print(li)