# 4881
import sys
sys.stdin = open('minsum_input.txt', 'r')

def backtrack(a, k, input):
    global MAXCANDIDATE
    global


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    print(M)

    def checknode(k):
        is promising

    for i in range(N):
        for j in range(i+1, N):
            if M[i][j] < M[i][j-1]:
                tmp = M[i][j]

minV = 100
a = [0] * (N+1)
backtrack(a, 0, N)
