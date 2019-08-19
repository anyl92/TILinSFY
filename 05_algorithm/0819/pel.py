#4861

import sys
sys.stdin = open('pel_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [list(input()) for _ in range(N)]

    if N == M:
        count = 0
        x = 0
        i = 0
        j = -1
        while x < N:
            if L[x][i] == L[x][j]:
                i += 1
                j -= 1
            else:
                x += 1
                continue
            if N % 2 and i == (N//2 +1):
                print(L[x])
                break
            elif i == (N//2):
                print(L[x])
                break

# 1번만 됨. 세로에 있는 펠린드롬 찾기, N!=M일 때 [0:N-M+1] 범위 포문, 스트링자르는건[M-N]