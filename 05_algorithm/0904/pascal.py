import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(N)
    C = [0*N for _ in range(N)]
    # for i in N:
    #     C = [0]*i
    #     C[0] = 1
    #     C[-1] = 1
    print(C)
        #
        # for i in range(2, N):
        #     for j in range(1, N):
