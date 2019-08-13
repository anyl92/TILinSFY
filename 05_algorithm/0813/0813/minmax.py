import sys
sys.stdin = open('sample_input.txt', 'r')

# def minmax(H):
#     return max(H)-min(H)

def minmax(H):
    Tmax = H[0]
    Tmin = H[0]
    for i in H:
        if Tmax < i:
            Tmax = i
        if Tmin > i:
            Tmin = i
    return Tmax-Tmin

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))

    res = minmax(H)
    print("#%d %d" % (tc, res))