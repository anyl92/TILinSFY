import sys
sys.stdin = open('binarysearch_input.txt', 'r')

def binarysearch(n):
    start = 1
    end = len(pages)
    count = 0
    middle = (start + end) // 2
    while middle != n:
        count += 1
        middle = (start + end) // 2
        if pages[middle] == n:
            return count
        elif pages[middle] > n:
            end = middle
        elif pages[middle] < n:
            start = middle

T = int(input())
for tc in range(1, T+1):
    a = list(map(int, input().split()))

    pages = [0] * a[0]
    for i in range(a[0]):
        pages[i] = i

    if binarysearch(a[1]) < binarysearch(a[2]):
        print('#%d %s' % (tc, 'A'))
    elif binarysearch(a[1]) > binarysearch(a[2]):
        print('#%d %s' % (tc, 'B'))
    else:
        print('#%d 0' % (tc))
