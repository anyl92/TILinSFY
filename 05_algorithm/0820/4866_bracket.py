import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    C = str(input())

    s = []
    top = -1
    for i in C:
        if '(' == i or '{' == i or '[' == i:
            s.append(i)
            top += 1
        elif (')' == i and s[-1] == '(') or ('}' == i and s[-1] == '{') or (']' == i and s[-1] == '['):
            if len(s) == 0:
                break
            s.pop()
            top -= 1

    if top == -1:
        print('#%d' % (tc), 1)
    else:
        print('#%d' % (tc), 0)

# '#%d' % (tc),