# 4874
import sys
sys.stdin = open('forth_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = list(map(str, input().split()))
    O = ['+', '-', '*', '/', '.']
    stack = []
    res = 0
    j = 0
    f = 1
    e = 0
    while f:
        for i in L:
            if i not in O:
                stack.append(i)
                j += 1
            elif i == '.':
                if len(stack)==1:
                    res = stack.pop()
                    f = 0
                    break
                else:
                    e = 1
                    f = 0
                    break
            else:
                if i == '*':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp1 * tmp2
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
                if i == '+':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp1 + tmp2
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
                if i == '-':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp2 - tmp1
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
                if i == '/':
                    if len(stack) > 1:
                        tmp1 = int(stack.pop(j-1))
                        tmp2 = int(stack.pop(j-2))
                        res = tmp2 // tmp1
                        stack.append(res)
                        j -= 1
                    else:
                        e = 1
                        f = 0
                        break
    if e:
        print('#%d' % (tc), 'error')
    else:
        print('#%d %d' % (tc, res))