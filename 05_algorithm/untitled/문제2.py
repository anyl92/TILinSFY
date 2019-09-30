def bfs():
    global count
    while queue:
        count += 1
        length = len(queue)

        for _ in range(length):
            point = queue.pop(0)

            for direction in range(4):
                idx = point[0]
                idy = point[1]
                idx += dx[direction]
                idy += dy[direction]

                if idx < 0 or idy < 0 or idx > 9 or idy > 9:
                    continue

                if board[idx][idy] == 0 or board[idx][idy] == 9:
                    queue.append([idx, idy])

                elif board[idx][idy] and not visited[idx][idy]:
                    visited[idx][idy] = 1
                    return


T = int(input())

for tc in range(1, T+1):

    t = int(input())

    board = [list(map(int, input().split())) for _ in range(10)]

    visited = [[0]*10 for _ in range(10)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 9:
                queue = []
                queue.append([i, j])
                count = 0
                bfs()
                result += count

    print('#{} {}'.format(tc, result))



