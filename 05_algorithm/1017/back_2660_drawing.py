import sys
sys.stdin = open('2660.txt', 'r')

N = int(input())
L = []
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        L += [a, b]

linked_list = [[] for _ in range(N+1)]
for i in range(len(L)//2):
    linked_list[L[2*i]].append(L[2*i+1])
    linked_list[L[2*i+1]].append(L[2*i])


def find(num, L):
    global mini
    q = [num]
    v = [0]* (N+1)
    v[num] = 1

    while q:
        c = q.pop(0)
        for i in range(len(L[c])):
            if v[L[c][i]] == 0:
                q.append(L[c][i])
                v[L[c][i]] = v[c]+1
    res = max(v)-1
    if mini > res:
        mini = res
    return res

cnt = 0
candi = []
res_list = []
mini = 999999999
for i in range(1, N+1):
    candi += [find(i, linked_list)]

for j in range(len(candi)):
    if candi[j] == mini:
        res_list += [j+1]
res_list.sort()

print(mini, len(res_list))
for j in res_list:
    print(j, end=' ')