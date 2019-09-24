import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]
    for i in range(len(L)//2):
        G[L[i * 2]].append(L[i * 2 + 1])
        G[L[i * 2 + 1]].append(L[i * 2])

    C = []
    for i in range(1, len(G)):
        G[i] += [i]
        C.append(G[i])
    print('C', C)

    res = []
    for i in range(1, N+1):
        tmp = []
        for j in C:
            if i in j:
                if sorted(j) not in tmp:
                    tmp.append(sorted(j))
        print('tmp', tmp)
        # if tmp not in res:
        #     res += tmp
        # print(res)

