#s2s3study.slack.com

import sys
sys.stdin = open('input.txt', 'r')

def DFS():
    if o == N:
        pass



N = int(input())
L = [[0 for _ in range(N)] for _ in range(N)]
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

start = L[0][0]