from itertools import combinations
print(list(combinations([1, 2, 3], 2)))


def perm(k):
    if k == r:
        print(T)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = i+1
            visited[i] = 1
            perm(k+1)
            visited[i] = 0

def pws(s):
    r = [[]]
    for e in s:
        tmp = [x+[e] for x in r]
        r += tmp
    return r

print(pws([1, 2, 3]))

def comb(k, s):
    if k == r:
        print(t)
    else:
        for i in range(s, N+(k-r)+1):
            t[k] = a[i]
            comb(k+1, i+1)

N = 6
r = 3
t = [0, 0, 0]
a = [1, 2, 3, 4, 5, 6]
comb(0, 0)