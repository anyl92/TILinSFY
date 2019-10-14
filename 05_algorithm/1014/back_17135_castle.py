import sys
sys.stdin = open('17135.txt', 'r')

# import itertools
# print(list(itertools.combinations([1,2,3,4,5],3)))


def comp(cnt):
    global res
    if res < cnt:
        res = cnt


def attack(T):
    cnt = 0
    for j in range(N-1, -1, -1):
        for i in range(D):
            if L[j-i]:
                for k in T:
                    if L[j-i][k]:
                        L[j-i][k] = 3
                        cnt += 1
            else:
                continue
    return cnt


def comb(k, s):
    if k == 3:
        for i in T:
            L[N][i] = 7

        comp(attack(T))

        for i in T:
            L[N][i] = 0

    else:
        for i in range(s, N+(k-3)+1):
            T[k] = P[i]
            comb(k+1, i+1)


N, M, D = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(M)] + [[0 for _ in range(N)]]

res, cnt = 0, 0

T = [0, 0, 0]
P = [0, 1, 2, 3, 4]

comb(0, 0)

print(res)