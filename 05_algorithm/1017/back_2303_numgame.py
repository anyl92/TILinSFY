import sys
sys.stdin = open('2303.txt', 'r')


def comb(k, s):
    global maxx
    if k == 3:
        res = 0
        for i in T:
            res += i
        tmp = int(str(res)[-1])
        if tmp > maxx:
            maxx = tmp
        return

    for i in range(s, len(use)+(k-3)+1):
        T[k] = use[i]
        comb(k+1, i+1)

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
T = [0]*3
max_list = []

for use in L:
    maxx = 0
    comb(0, 0)
    max_list += [maxx]

cnt = 0
res_list = []
for j in max_list:
    if j == max(max_list):
        res_list += [-10]
    else:
        res_list += [0]

k = res_list.count(-10)
if k == 1:
    print(res_list.index(-10) + 1)
else:
    for i in range(len(res_list)-1, -1, -1):
        if res_list[i] == -10:
            print(i+1)
            break