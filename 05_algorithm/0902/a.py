import sys
sys.stdin = open('order_input.txt', 'r')

for tc in range(3):
    result = []
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    L = [tmp[2*i:2*i+2] for i in range(E)]
    print(L)

    visited = [0] * (V+1)
    checked = [0] * (V+1)

    start_pt =[]


    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][0] == L[j][1]:
                break
        else:
            start_pt.append(L[i][0])

    print(start_pt)