import sys
sys.stdin = open('input.txt', 'r')

def find(H):
    left = right = comp = tot = now = 0
    left_1 = left_2 = right_1 = right_2 = 0
    for i in range(2, len(H)-2):
        now = H[i]
        right_1 = H[i+1]
        right_2 = H[i+2]
        left_1 = H[i-1]
        left_2 = H[i-2]

        if now > left_1 and now > right_1:
            if now > left_2 and now > right_2:
                if right_1 >= right_2:
                    right = right_1
                else:
                    right = right_2
                if left_1 >= left_2:
                    left = left_1
                else:
                    left = left_2
                if right >= left:
                    comp = right
                else:
                    comp = left
                tot += (now - comp)
        else:
            pass
    return tot

T = 10
# T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))

    res = find(H)
    print("#%d %d" % (tc, res))