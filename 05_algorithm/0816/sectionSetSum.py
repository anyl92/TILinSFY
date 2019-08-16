import sys
sys.stdin = open('sectionSetSum_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    count = 0
    setlist = list(range(1, 13))
    for i in range(1, 1 << len(setlist)):
        subset = []
        subres = 0
        for j in range(len(setlist)):
            if i & (1 << j):
                subset.append(setlist[j])
        if len(subset) == N[0]:
            for k in range(len(subset)):
                subres += subset[k]
            if subres == N[1]:
                count += 1

    print('#%d %d' % (tc, count))