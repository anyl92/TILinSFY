import sys
sys.stdin = open('input.txt', 'r')

def perm(k, temp=100):
    global maxx, N
    if k == N:
        if maxx < temp:
            maxx = temp
    else:
        for i in range(k, N):
            P[k], P[i] = P[i], P[k]
            if temp*L[k][P[k]] > maxx:
                perm(k+1, temp*L[k][P[k]])
            P[k], P[i] = P[i], P[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    P = [i for i in range(N)]
    # print(P) # 0, 1, 2, 3
    maxx = 0
    for i in range(N):
        for j in range(N):
            L[i][j] *= 0.01
    perm(0)
    print(maxx)