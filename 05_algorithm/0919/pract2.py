a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(a)
t = [0]*N
visited = [0]*N
visited2 = []

def perm(k):
    if k == N:
        summ = 0
        set = []
        for i in t:
            summ += i
            set.append(i)
            if summ == 10:
                set.sort()
                if set in visited2:
                    continue
                visited2.append(set)
                break
            elif summ > 10:
                break

    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = a[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0

perm(0)
print(visited2)
print(len(visited2))
