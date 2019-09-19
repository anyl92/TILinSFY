import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    conta, truck = list(map(int, input().split()))
    wei = list(map(int, input().split()))
    fil = list(map(int, input().split()))

    wei = (sorted(wei))[::-1]
    fil = (sorted(fil))[::-1]

    summ = 0
    for i in range(len(wei)):
        for j in range(len(fil)):
            if fil[j] >= wei[i]:
                fil[j] = 0
                summ += wei[i]
                break
            else:
                continue
    print('#%d %d' % (tc, summ))