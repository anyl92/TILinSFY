import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    # 흰색 1, 검은색 0
    #print(N, K, L)

    j, k, count, res = 0, 0, 0, 0
    for i in range(N):
        while j+k < N:
            k = 0
            if L[i][j] == 1:
                while k+j < N and L[i][j+k] == 1:
                    count += 1
                    k += 1
                j += k-1
            if count == K:
                res += 1
                count = 0
            j += 1
            count = 0
        j = 0
    print(res)

    i, k, count = 0, 0, 0
    while i+k < N:
        for j in range(N):
            k = 0
            if L[i][j] == 1:
                while k+i < N and L[i+k][j] == 1:

