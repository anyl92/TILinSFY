import sys
sys.stdin = open('delete_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    L = list(map(str, input()))
    i = 1
    while i < len(L):
        if len(L) < 2:
            break
        if L[i-1] == L[i]:
            L.pop(i)
            L.pop(i-1)
            if i==1:
                continue
            i -= 1
        else:
            i += 1
    print('#%d %d' % (tc, len(L)))