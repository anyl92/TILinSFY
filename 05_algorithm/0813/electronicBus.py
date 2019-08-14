import sys
sys.stdin = open('sample_input(1).txt', 'r')

def Charge(N, H):
    count = bus = check = 0
    cango = N[0]
    rlist = []
    tlist = []
    while bus < N[1]:
        if N[1] < check + cango:
            return count

        check = bus + cango
        if N[1] == check:
            return count

        rlist = list(range(bus + 1, check + 1))
        pre = len(tlist)
        for i in rlist:
            if i in H:
                tlist.append(i)

        if len(tlist) == pre:
            return 0

        bus = max(tlist)
        count += 1

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    H = list(map(int, input().split()))

    res = Charge(N, H)
    print("#%d %d" % (tc, res))