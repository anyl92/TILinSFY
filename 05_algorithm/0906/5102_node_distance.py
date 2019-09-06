import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(E)]
    G = list(map(int, input().split()))
    # print(V, E, L, G)

    visited = [0] * (V+1)
    q = [G[0]]
    # print(q)

    visited[G[0]] = 1
    # print(visited)

    end = False
    count = 0
    while not end and q:
        result = 0
        stp = []
        while q:
            stp.append(q.pop(0))
        for j in range(len(stp)):
            for i in range(len(L)):
                if stp[j] in L[i]:
                    if G[1] in L[i]:
                        result = count
                        end = True
                        break
                    else:
                        tmp = L[i].index(stp[j])
                        q.append(L[i][abs(tmp-1)])
            if end:
                break
        count += 1

    print('#%d %d' % (tc,count))


