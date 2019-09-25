import sys
sys.stdin = open('input.txt', 'r')


def calc(T):
    start = T[:N//2]
    link = T[N//2:]
    SA, LA = 0, 0

    for i in range(len(start)-1):
        for j in range(i+1, len(start)):
            SA += L[start[i]][start[j]]
            SA += L[start[j]][start[i]]
            LA += L[link[i]][link[j]]
            LA += L[link[j]][link[i]]
    tmp = abs(SA-LA)

    return tmp


def perm(k):
    global mini
    if k >= N:
        tmp = calc(T)
        if mini > tmp:
            mini = tmp
        return

    for i in range(k, N):
        T[k], T[i] = T[i], T[k]
        perm(k + 1)
        T[k], T[i] = T[i], T[k]


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
T = [i for i in range(N)]
mini = 999999

perm(0)
print(mini)