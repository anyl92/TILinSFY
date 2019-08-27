def bfs(arr, v):
    visited = [0]*8
    q = []
    q.append(v)
    while q:
        t = q.pop(0)
        # print('t', t)
        if not visited[t]:
            visited[t] = True
            print(t)
        for i in range(len(arr[t])):
            if arr[t][i] == 1 and not visited[i]:
                q.append(i)
​
​
s = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
arr = [[0]*8 for _ in range(8)]
​
for n in range(0, len(s), 2):
    arr[s[n]][s[n+1]] = 1
    arr[s[n+1]][s[n]] = 1
​
print(arr)
bfs(arr, 1)