import sys
sys.stdin = open('input.txt', 'r')



T = int(input())
for tc in range(1, T+1):
    N, per = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    chk = [0 for _ in range(N)]
    L = sorted(L)
    CL = sorted(L)
    print(L, CL, chk)

    