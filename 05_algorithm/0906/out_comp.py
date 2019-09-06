import sys
sys.stdin = open('input.txt', 'r')

def solve(k):
    global ans
    if k == N:
        for i in range(N):
            if Si[i]:
                for j in range(i+1, i+Ti[i]):  # i+1부터 i+T까지
                    if j >= N or Si[j]:  # j가 N보다 크면 종료, S의 j번째가 1이면 종료
                        return
        tsum = 0
        for i in range(N):
            if Si[i]:
                tsum += Pi[i]
        if tsum > ans:
            ans = tsum

    else:
        Si[k] = 1
        # print(Si)
        solve(k+1)
        Si[k] = 0
        # print(Si)
        solve(k+1)

N = int(input())
Ti = [0]*N
Pi = [0]*N
Si = [0]*N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())

ans = 0
solve(0)

print(ans)