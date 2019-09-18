import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    conta, truck = list(map(int, input().split()))
    wei = list(map(int, input().split()))
    fil = list(map(int, input().split()))
    # print(conta, truck, wei, fil)

    wei = (sorted(wei))[::-1]
    fil = (sorted(fil))[::-1]
    # print(wei, fil)

    wei_x, fil_x = [], []

    for i in range(len(wei)):
        for j in range(i+1, len(wei)):
            if (wei[i]+wei[j]) in fil:
                a = fil.index(wei[i] + wei[j])
                wei_x += [i, j]
                fil_x += [a]
    print(wei_x, fil_x)
    for x in wei_x:


