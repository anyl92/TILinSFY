import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [str(input()) for _ in range(N)]
    # print(L)
    code = [
        '0001101',
        '0011001',
        '0010011',
        '0111101',
        '0100011',
        '0110001',
        '0101111',
        '0111011',
        '0110111',
        '0001011',
    ]

    def find_code(tmp):
        section = []
        for i in range(8):
            section += [tmp[i*7:(i*7)+7]]
        print(section)
        res = ''
        for j in section:
            for i in code:
                if i == j[0:7]:
                    res += str(code.index(i))
        print(res)
        even = 0
        total = 0
        for k in range(len(res)):
            if k == len(res)-1:
                total += int(res[k])
            elif k % 2 == 0:  # 짝
                even += int(res[k])
            else:
                total += int(res[k])
        total += even*3
        if total % 10 == 0:
            c = 0
            for l in res:
                c += int(l)
            return c
        return 

    number = ''
    for y in range(N-1, -1, -1):
        for x in range(M-1, -1, -1):
            if L[y][x] == '1':
                tmp = L[y][x-55:x+1]
                number += find_code(tmp)