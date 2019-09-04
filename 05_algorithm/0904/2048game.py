import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(str, input().split())
    L = [list(map(int, input().split())) for _ in range(int(N))]
    print(N, M, L)

