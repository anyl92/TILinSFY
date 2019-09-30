def remain(s, C):

    for r in range(s, len(minerals)):
        if C - (abs(robot[0]-minerals[r][0])+abs(robot[1]-minerals[r][1]))*2 >= 0:
            return False

    return True

def backtrack(s, result, C):
    global robot, mineral
    global max_result

    if remain(s, C):
        if max_result < result:
            max_result = result

    else:
        for m in range(s, len(minerals)):
            if (abs(robot[0]-minerals[m][0])+abs(robot[1]-minerals[m][1]))*2 <= C:
                backtrack(m+1, result+minerals[m][2], C-(abs(robot[0]-minerals[m][0])+abs(robot[1]-minerals[m][1]))*2)


T = int(input())

for tc in range(1, T+1):

    N, M, C = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(M)]

    minerals = []
    max_result = 0
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                robot = [i, j]
            elif board[i][j]:
                minerals.append([i, j, board[i][j]])

    visited = [0]*len(minerals)
    result = 0
    backtrack(0, result, C)

    print('#{} {}'.format(tc, max_result))



