import sys
sys.stdin = open('pel2_input.txt')

for tc in range(1, 11):
    N = int(input())
    L = [list(input()) for _ in range(100)]
    #print(L)
    flag = 1
    l = 3
    while l < 100:
        li = [0] * l
        while flag:
            for i in range(100):  # 행
                for j in range(100-l):  # 열
                    for k in range(N - i - 1):  # 회문검사범위
                        li[k] = L[i][k+j]  # 리스트에추가
                        if l == l[::-1]:  # 회문검사
                            l += 1  # 회문검사할 길이증가
                            flag = 1  # 회문이면 플래그
                        else:
                            flag = 0
                            break

