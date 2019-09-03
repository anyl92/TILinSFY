import sys
sys.stdin = open('order_input.txt', 'r')

def start(L):
    stp = []
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][0] == L[j][1]:
                break
        else:
            stp += [L[i][0]]
    return list(set(stp))

for tc in range(1, 11):
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    L = [tmp[2 * i:2 * i + 2] for i in range(E)]
    # print(L)
    # print(start(L))
    visited = [i for i in range(1, V+1)]

    stack = []
    stp = start(L)
    path = []
    for i in range(len(stp)):
        stack.append(stp[i])

    while stack:
        current = stack.pop(-1)
        trash = []

        for edge in L:
            if current == edge[1]:
                break
        else:
            path.append(current)

            for edge in L:
                if current == edge[0]:
                    stack.append(edge[1])
                    trash.append(edge)

            for t in trash:
                L.remove(t)

    print('#{} {}'.format(tc, ' '.join(list(map(str,path)))))

