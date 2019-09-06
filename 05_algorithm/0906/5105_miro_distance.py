import sys
sys.stdin = open('input.txt', 'r')

def wall(next, l):
    return next[0] < 0 or next[1] < 0 or next[0] >= len(l) or next[1] >= len(l) or (l[next[0]][next[1]])==1

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    l = [list(map(int, input())) for _ in range(n)]

    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    count = 0
    result = 0
    end = False
    q = []

    for i in range(n):
        for j in range(n):
            if l[i][j] == 2:
                q.append([i, j])
                break

    while not end and q:
        current = []
        while q:
            current.append(q.pop(0))
        for c in current:
            for d in dir:
                next = [c[0]+d[0], c[1]+d[1]]
                if wall(next, l):
                    pass
                elif l[next[0]][next[1]] == 3:
                    result = count
                    end = True
                    break
                else:
                    l[next[0]][next[1]] = 1
                    q.append(next)
        count += 1
    print('#%d %d' % (tc, result))