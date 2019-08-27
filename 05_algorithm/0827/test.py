import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0 for _ in range(M)] for _ in range(N)]

    # print(arr[1][1])
    x = [0]
    f = 0
    for k in range(K):
        x.append(L[k][4])
        if L[k][0] == L[k][2]:
            y = 1
            for i in range(y):
                for j in range(L[k][1], L[k][3]+1):
                    if not arr[i][j] > L[k][4]:
                        arr[i][j] = L[k][4]

        for i in range(L[k][0], L[k][2]+1):
            for j in range(L[k][1], L[k][3]+1):
                if arr[i][j] > L[k][4]:
                    f = 1
                    break
            if f:
                break
        if f == 0:
            for i in range(L[k][0], L[k][2]+1):
                for j in range(L[k][1], L[k][3]+1):
                    arr[i][j] = L[k][4]
        f = 0

    count = [0]*11
    for n in set(x):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == n:
                    count[n] += 1
    print('#%d %d' % (tc, max(count)))


# 런타임 에러가 발생하였습니다. 런타임 에러로 전체 혹은 일부 테스트 케이스는 채점이 되지 않을 수 있습니다.
# Error Message :
# Traceback (most recent call last):
#   File "/solution.py", line 13, in <module>
#     if arr[i][j] > L[k][4]:
# IndexError: list ind