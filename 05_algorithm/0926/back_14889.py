import sys
sys.stdin = open('14889_input.txt', 'r')


def calc(A):
    global mini
    start = A
    link = []
    for i in T:
        if i not in A:
            link.append(i)

    SA, LA = 0, 0
    for i in range(len(start)-1):
        for j in range(i+1, len(start)):
            SA += L[start[i]][start[j]]
            SA += L[start[j]][start[i]]
            LA += L[link[i]][link[j]]
            LA += L[link[j]][link[i]]
    tmp = abs(SA-LA)

    if mini > tmp:
        mini = tmp


def comb(k, s):
    if k == R:
        calc(A)
    else:
        for i in range(s, N+(k-R)+1):
            A[k] = T[i]
            comb(k+1, i+1)


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

A = [0] * (N//2)
T = [i for i in range(N)]
mini = 999999
R = N//2
comb(0, 0)

print(mini)