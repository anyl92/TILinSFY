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
        for i in range(7):
            section += [tmp[i*8:(i*8)+8]]
        print(section)
        res = ''
        for j in section:
            for i in code:
                if i == j[0:7]:
                    res += str(code.index(i))
        print(res)

    number = ''
    for y in range(N-1, -1, -1):
        for x in range(M-1, -1, -1):
            if L[y][x] == '1':
                tmp = L[y][x-55:x+1]
                print(tmp)
                number += find_code(tmp)
        # odd = 0
        # for i in range(len(number)-1):
        #     if i % 2:  # 홀
        #         odd += number[i]
        #     else:
        #         res += number[i]
        # res = res + odd + number[-1]
        # res +=