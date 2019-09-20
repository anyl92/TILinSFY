import sys
sys.stdin = open('input.txt', 'r')

def find_min():
    global L, CL, chk, tmp_li
    minn = 999
    tmp_li = []
    for i in range(len(CL)):
        if chk[i]:
            tmp_li += [CL[i] + L[i]]
        else:
            print(i)
            tmp_li += [CL[i]]
    print(tmp_li,'tmp')
    return tmp_li


T = int(input())
for tc in range(1, T+1):
    N, per = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    chk = [0 for _ in range(N)]
    # print(N, per)
    L = sorted(L)
    CL = sorted(L)
    print(L, CL, chk)
    # print(sort_L.index(min(sort_L)))
    cnt = 0
    while per:
        tmp_li = find_min()
        chk[tmp_li.index(min(tmp_li))] += 1
        for i in range(len(chk)):
            for j in range(L[i]-1):
                cnt += 1
                CL[j] -= 1
                # tmp = CL.index(i)
                print(CL, L)
        per -= 1
    print(chk, per)