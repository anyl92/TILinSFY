import sys
sys.stdin = open('16236.txt', 'r')

import collections

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


def find(i, j):
    global shark_size, bigger, flag
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dq = collections.deque([(i, j)])
    V = [[0]*N for _ in range(N)]
    V[i][j] = 1
    time = 0

    while dq:  # dq가 있을때
        fish = collections.deque([])
        for _ in range(len(dq)):  # dq의 갯수만큼
            current = dq.popleft()  # 현재위치팝
            for d in dir:  # 4방향
                ii = current[0] + d[0]
                jj = current[1] + d[1]
                if 0 <= ii < N and 0 <= jj < N:  # 행렬 범위 내에서
                    if V[ii][jj] == 0:  # visited 아니고
                        tmp = L[ii][jj]
                        if L[ii][jj] > shark_size:
                            continue  # 사이즈 크면 다음 방향으로
                        if L[ii][jj] == 0 or L[ii][jj] == shark_size:  # 0이거나 크기가같으면
                            dq.append((ii, jj))  # 다음 dq볼 때
                            V[ii][jj] = 1  # visited 체크
                        elif L[ii][jj] < shark_size:  # 나보다 작을때 #and bigger+tmp <= shark_size
                            fish.append((ii, jj))  # 물고기 배열에 추가
                            dq.append((ii, jj))
                            V[ii][jj] = 1
        time += 1  # 이동거리 체크

        if fish:  # 먹을 물고기 있으면
            L[i][j] = 0  # 상어 원래위치를 0으로 만듬
            change = sorted(fish)[0]  # 먹을 수 있는 걸 정렬해서 가장 처음 거 먹음
            bigger += 1  # 상어 크게 만들어줄 변수

            if bigger == shark_size:  # 상어 크기랑 같으면
                bigger = 0  # 초기화하고
                shark_size += 1  # 키워줌

            L[change[0]][change[1]] = 9  # 물고기 먹은 자리로 이동
            flag = 1
            return time  # 리턴하고 다시 돌아야함

    else:  # 먹을 물고기없음
        flag = 0
        time = 0
        return time  # -1 리턴해서 0출력


flag = 1
bigger = 0
shark_size = 2
res = 0

while flag:
    f = 0
    for i in range(N):
        for j in range(N):
            if L[i][j] == 9:
                res += find(i, j)
                f = 1
                break
        if f:
            break
print(res)