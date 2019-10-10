import sys
sys.stdin = open('2630.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


def divi(N, L):
    if N == 1:
        return

    dir = [(0, N//2), (N//2, N)]
    for comb in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        lis = []
        for i in range(dir[comb[0]][0], dir[comb[0]][1]):
            li = []
            for j in range(dir[comb[1]][0], dir[comb[1]][1]):
                li += [L[i][j]]
            lis += [li]
        if counting(len(lis[0]), lis):
            divi(N//2, lis)
    else:
        return


def counting(N, L):
    global blue, white
    flag = False

    tmp = L[0][0]
    for i in range(N):
        for j in range(N):
            if tmp != L[i][j]:
                flag = True
                break
        if flag:
            return 1
    else:
        if L[0][0] == 1:
            blue += 1
        else:
            white += 1


    # blue_cnt, white_cnt = 0, 0
    # for i in range(N):
    #     for j in range(N):
    #         if L[i][j] == 1:
    #             blue_cnt += 1
    #         else:
    #             white_cnt += 1
    #
    # if N**2 == blue_cnt or N**2 == white_cnt:
    #     if N**2 == blue_cnt:
    #         blue += 1
    #     if N**2 == white_cnt:
    #         white += 1
    #     return 0
    # else:
    #     return 1


blue, white = 0, 0

if counting(N, L):
    divi(N, L)
print(white)
print(blue)