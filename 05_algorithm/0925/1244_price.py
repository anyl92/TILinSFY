import sys
sys.stdin = open('input.txt', 'r')


def find(cnt, N, int_N, V):
    global maxx
    if cnt == M:
        if maxx < int_N:
            maxx = int_N
        return

    for i in range(len(N)):
        for j in range(len(N)):
            if i != j:
                N[i], N[j] = N[j], N[i]
                int_N = int(''.join(N))
                if cnt != M-1:
                    if not V[int_N]:
                        V[int_N] = 1
                        cnt += 1
                        find(cnt, N, int_N, V)
                        cnt -= 1
                    N[i], N[j] = N[j], N[i]
                else:
                    cnt += 1
                    find(cnt, N, int_N, V)
                    cnt -= 1
                    N[i], N[j] = N[j], N[i]


T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    M = int(M)
    N = list(N)
    int_N = int(''.join(N))
    maxx = 0
    V = [0] * 1000000
    V[int_N] = 1

    find(0, N, int_N, V)
    print('#%d %d' % (tc, maxx))