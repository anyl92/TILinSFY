import sys
sys.stdin = open('17135.txt', 'r')


def find(r, c, k):
    if k == D-1:
        return

    tmp_max = 0
    tmp_list = []
    dir = [(-1, 0), (0, -1), (0, 1)]  # 상, 좌, 우
    for d in dir:
        rr = r + d[0]
        cc = c + d[1]
        if 0 <= rr < N and 0 <= cc < M:
            if L[rr][cc]:
                tmp = cc
                if tmp_max <= tmp:
                    tmp_max = tmp
                    tmp_list += [(rr, cc)]
                    return tmp_list
            else:
                find(rr, cc, k+1)


def attack(T, r):
    max_cnt = 0
    attack_list = []
    for c in T:  # 0, 1, 2   c는 궁수 자리 열
        if L[r][c]:  # 궁수 열 위치에서 처음 적군이 자리에 있는지 확인  여기가 무조건 첫자리
            attack_list += [(r, c)]  # 어택 리스트에 좌표 추가(행, 열)
        else:  # 없으면 다음 이동거리를 찾아감
            for l in range(D-1):  # 이동거리가 있으면 -1 한만큼 반복함
                dir = [(-1, 0), (0, -1), (0, 1)]  # 상, 좌, 우
                for d in dir:
                    rr = r + d[0]
                    cc = c + d[1]
                    if 0 <= rr < N and 0 <= cc < M:  # 행열이 배열 범위를 넘어가지 않으면
                        if L[rr][cc]:  # 값이 있으면
                            attack_list += [(rr, cc)]
                            break  # for문을 나가 다음 방향을 본다

    for a in attack_list:  # 어택 리스트에 들어있는 좌표들의 값을 0으로 바꾼다
        L[a[0]][a[1]] = 0

    if len(set(attack_list)) > max_cnt:  # 중복을 없애고 갯수를 세서 최대값만 저장되게 한다
        max_cnt = len(set(attack_list))

    return max_cnt


def locate(k, s):  # 궁수 위치를 조합으로 구함
    global res

    if k == 3:
        cnt = 0  # 조합 배열이 구해졌을 때 cnt를 초기화
        for j in range(N-1, -1, -1):  # 턴마다 적군을 죽이기 위해 4, 3, 2, 1, 0
            cnt += attack(T, j)  # 배열 T와 현재 행 j를 가지고 attack, 리턴값을 cnt에 누적 저장

            for l in range(M):
                if L[j][l]:
                    L[j][l] = 0

        if cnt > res:
            res = cnt

        for x in range(N):
            for y in range(M):
                L[x][y] = CL[x][y]

    else:
        for i in range(s, M+(k-3)+1):
            T[k] = P[i]
            locate(k+1, i+1)


N, M, D = list(map(int, input().split()))  # 행, 열, 공격 거리
L = [list(map(int, input().split())) for _ in range(N)]
CL = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        CL[i][j] = L[i][j]

res, cnt = 0, 0

T = [0, 0, 0]  # 조합이 저장될 배열
P = [i for i in range(N)]  # 조합을 구할 수를 구한 배열 (0, 1, 2, 3, 4)

locate(0, 0)  # 조합 k, s

print(res)