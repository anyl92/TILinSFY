import sys
sys.stdin = open('14889_input.txt', 'r')


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


# def perm(k):
#     global mini
#     if k == N//2:
#         print(T)
#         tmp = calc(T)
#         if mini > tmp:
#             mini = tmp
#         return
#
#     for i in range(N//2, N):
#
#         T[k], T[i] = T[i], T[k]
#         perm(k + 1)
#         T[k], T[i] = T[i], T[k]


def perm(k, m):
    global mini
    if k == N//2:
        print(T)
        tmp = calc(T)
        if mini > tmp:
            mini = tmp
        return

    for i in range(m, N):
        T[k], T[i] = T[i], T[k]
        perm(k + 1, i)
        T[k], T[i] = T[i], T[k]

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
T = [i for i in range(N)]
mini = calc(T)

# perm(0)
perm(0, N//2)
print(mini)

# print(T)
# start = []
# for i in range(len(T)):
#     for j in range(1+i, len(T)):
#         start += [T[i]]
#         start += [T[j]]
#         print(start)