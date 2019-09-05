import sys
sys.stdin = open('input.txt', 'r')

def pushup(N, L):
    j, k, cnt = 0, 0, 0
    for i in range(N):
        while j < N-1:
            if L[j][i] == 0:
                k = j
                while j < N-1 and L[j+1][i] == 0:
                    j += 1
                    cnt += 1
                if j == N-1:
                    cnt = 0
                    break
                L[k][i] = L[j+1][i]
                L[j+1][i] = 0
                if cnt > 0:
                    j -= cnt
            j += 1
            cnt = 0
        j = 0
    return L

def pushdown(N, L):
    j, k, cnt = N-1, 0, 0
    for i in range(N):
        while 0 < j:
            if L[j][i] == 0:
                k = j
                while 0 < j and L[j-1][i] == 0:
                    j -= 1
                    cnt += 1
                if j == 0:
                    cnt = 0
                    break
                L[k][i] = L[j-1][i]
                L[j-1][i] = 0
                if cnt > 0:
                    j += cnt
            j -= 1
            cnt = 0
        j = N-1
    return L

def pushleft(N, L):
    j, k, cnt = 0, 0, 0
    for i in range(N):
        while j < N-1:
            if L[i][j] == 0:
                k = j
                while j < N-1 and L[i][j + 1] == 0 :
                    j += 1
                    cnt += 1
                if j == N-1:
                    cnt = 0
                    break
                L[i][k] = L[i][j+1]
                L[i][j+1] = 0
                if cnt > 0:
                    j -= cnt
            j += 1
            cnt = 0
        j = 0
    return L

def pushright(N, L):
    j, k, cnt = N-1, 0, 0
    for i in range(N):
        while 0 < j:
            if L[i][j] == 0:
                k = j
                while 0 < j and L[i][j - 1] == 0:
                    j -= 1
                    cnt += 1
                if j == 0:
                    cnt = 0
                    break
                L[i][k] = L[i][j-1]
                L[i][j-1] = 0
                if cnt > 0:
                    j += cnt
            j -= 1
            cnt = 0
        j = N-1
    return L

def sumup(N, L):
    for i in range(N):
        for j in range(N-1):
            if L[j][i] == L[j+1][i] and L[j][i] != 0:
                L[j][i] += L[j+1][i]
                L[j+1][i] = 0
    return L

def sumdown(N, L):
    for i in range(N):
        for j in range(N-1, 0, -1):
            if L[j][i] == L[j-1][i] and L[j][i] != 0:
                L[j][i] += L[j-1][i]
                L[j-1][i] = 0
    return L

def sumleft(N, L):
    for i in range(N):
        for j in range(N-1):
            if L[i][j] == L[i][j+1]:
                L[i][j] += L[i][j+1]
                L[i][j+1] = 0
    return L

def sumright(N, L):
    for i in range(N):
        for j in range(N-1, 0, -1):
            if L[i][j] == L[i][j-1]:
                L[i][j] += L[i][j-1]
                L[i][j-1] = 0
    return L


T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    N = int(N)
    L = [list(map(int, input().split())) for _ in range(int(N))]

    if M == 'up':
        pushup(N, L)
        sumup(N, L)
        pushup(N, L)
    elif M == 'down':
        pushdown(N, L)
        sumdown(N, L)
        pushdown(N, L)
    elif M == 'left':
        pushleft(N, L)
        sumleft(N, L)
        pushleft(N, L)
    elif M == 'right':
        pushright(N, L)
        sumright(N, L)
        pushright(N, L)

    print('#%d' % tc)
    for i in L:
        for j in i:
            print(str(j), end=' ')
        print()