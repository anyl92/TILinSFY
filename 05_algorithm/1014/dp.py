import sys
sys.stdin = open('dp.txt', 'r')

x = 10
dp = [0 for _ in range(x+1)]

dp[1] = 0
print(dp)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[x])