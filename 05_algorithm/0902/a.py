import sys
sys.stdin = open('order_input.txt', 'r')

def stack_cal(stack):
    k = 0
    while k < len(stack):
        if stack == []:
            return False
        if stack[-1] == L[k][0]:
            stack.append(L[k][1])
        k += 1
    k = 0
    return stack


for tc in range(10):
    result = []
    V, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    L = [tmp[2*i:2*i+2] for i in range(E)]
    print(L)

    visited = [0] * (V+1)
    checked = [0] * (V+1)

    start_pt = []
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][0] == L[j][1]:
                break
        else:
            start_pt.append(L[i])
    print(start_pt)

    stack = [start_pt[0][0]]
    for k in range(len(L)):
        if stack[-1] == L[k][0]:
            stack.append(L[k][1])
    print(stack)
    print(stack_cal(stack))

