import sys
sys.stdin = open('rabbit_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    steps = 0
    i = 3
    x, y = 0, 0

    while -1 < y+dy[i] < 10 or -1 < x+dx[i] < 10:  # y와 x의 범위는 0부터 9까지(배열크기)
        while L[y][x] == 0:  # 원소가 0일 때
            if x+dx[i] == 10 or x+dx[i] == -1 or y+dy[i] == -1 or y+dy[i] == 10:
                break  # 다음 위치가 배열을 벗어나면 break
            x += dx[i]
            y += dy[i]
            steps += 1  # 다음 위치로 이동하며 스텝 증가
        if L[y][x] == 2:  # 원소가 2일 때 방향을 바꿔줌
            if i == 3:
                i = 1
            elif i == 2:
                i = 0
            elif i == 1:
                i = 3
            elif i == 0:
                i = 2
        elif L[y][x] == 1:  # 원소가 1일 때 방향을 바꿔줌
            if i == 3:
                i = 0
            elif i == 2:
                i = 1
            elif i == 1:
                i = 2
            elif i == 0:
                i = 3
        x += dx[i]  # 방향을 바꿔준 뒤 다음 위치로 이동하며 스텝 증가
        y += dy[i]
        steps += 1
        if x > 9 or x < 0 or y < 0 or y > 9:  # x와 y의 위치가 0보다 작거나 9보다 크면 전체 break
            break

    print(steps-1)  # 마지막 위치에서 steps를 증가시켜줬기 때문에 다시 -1해줌
