import sys
sys.stdin = open('sample_input(2).txt', 'r')

def sectionSum(N, H):
    sum_str = 0
    sum_list = []
    for i in range(N[1]):
        sum_str += H[i]
    sum_list.append(sum_str)

    for j in range(N[1], len(H)):
        sum_str = sum_str + H[j] - H[j-N[1]]
        sum_list.append(sum_str)

    return max(sum_list) - min(sum_list)

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    H = list(map(int, input().split()))

    res = sectionSum(N, H)
    print("#%d %d" % (tc, res))