import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]

    sum_cnt = 0
    sum_list = []
    for x in range(N-M+1):
        for y in range(N-M+1):
            for i in range(M):
                for j in range(M):
                    sum_cnt += L[i+x][j+y]
            sum_list.append(sum_cnt)
            sum_cnt = 0
    print(max(sum_list))