import sys
sys.stdin = open('2798_input.txt', 'r')

def comb(k, s, res):
    global mini, ans

    if k == 3:
        if abs(res - M) < mini:
            mini = abs(res - M)
            ans = res

    else:
        for i in range(s, N):
            res += L[i]
            if res <= M:
                comb(k+1, i+1, res)
            res -= L[i]

N, M = map(int, input().split())
L = list(map(int, input().split()))
mini = 999999999999
ans = 0
comb(0, 0, 0)
print(ans)
