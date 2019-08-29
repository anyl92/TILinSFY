import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(str, input())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 0

    def find(F):
        if F == 'A':
            for k in range(4):
                if L[j + dy[k]][i + dx[k]] == 'H':
                    L[j + dy[k]][i + dx[k]] = 'Z'
        elif F == 'B':
            for n in range(2):
                for k in range(4):
                    if L[j + dy[k] + n][i + dx[k] + n] == 'H':
                        L[j + dy[k] + n][i + dx[k] + n] = 'Z'
        elif F == 'C':
            for n in range(3):
                for k in range(4):
                    if L[j + dy[k] + n][i + dx[k] + n] == 'H':
                        L[j + dy[k] + n][i + dx[k] + n] = 'Z'

    for j in range(len(L)):
        for i in range(len(L)):
            if L[j][i] == 'A':
                find(L[j][i])

    for j in range(len(L)):
        for i in range(len(L)):
            if L[j][i] == 'H':
                cnt += 1
    print(cnt)