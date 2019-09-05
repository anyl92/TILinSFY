import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    # print(N, L)

    up = ''
    i = 0
    while i < N:
        for j in range(N-1, -1, -1):
            up += str(L[j][i])
        i += 1
    # print(up)

    garo = ''
    for j in range(N-1, -1, -1):
        for i in range(N-1, -1, -1):
            garo += str(L[j][i])
    # print(garo)

    down = ''
    i = N - 1
    while i > -1:
        for j in range(N):
            down += str(L[j][i])
        i -= 1
    # print(down)

    print('#%d' % tc)
    for k in range(len(garo)//N):
        result = up[N*k:N+(N*k)] + ' ' + garo[N*k:N+(N*k)] + ' ' + down[N*k:N+(N*k)]
        print(result)