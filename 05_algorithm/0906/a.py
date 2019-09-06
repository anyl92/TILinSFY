import sys
sys.stdin = open('input.txt', 'r')

def is_wall(pt, maze):
    return pt[0] < 0 or pt[1] < 0 or pt[0] >= len(maze) or pt[1] >= len(maze) or maze[pt[0]][pt[1]] == 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    is_end = False
    count = 0
    result = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q = [(i, j)]
                break

    while not is_end and q:
        current = []
        while q:
            current.append(q.pop(0))

        for cur in current:
            for direction in directions:
                next_pt = (cur[0]+direction[0], cur[1]+direction[1])
                if is_wall(next_pt, maze):
                    pass
                elif maze[next_pt[0]][next_pt[1]] == 3:
                    result = count
                    is_end = True
                    break
                else:
                    maze[next_pt[0]][next_pt[1]] = 1
                    q.append(next_pt)
        count += 1

    print('#{} {}'.format(t, result))