# 4880
import sys
sys.stdin = open('card_input.txt', 'r')

def RSP(a, b):
    if a[0] == 1:
        if b[0] == 1:
            if a[0] < b[0]:
                winner = a
            else:
                winner = b
        elif b[0] == 2:
            winner = b
        elif b[0] == 3:
            winner = a
    elif a[0] == 2:
        if b[0] == 1:
            winner = a
        elif b[0] == 2:
            if a[0] < b[0]:
                winner = a
            else:
                winner = b
        elif b[0] == 3:
            winner = b
    elif a[0] == 3:
        if b[0] == 1:
            winner = b
        elif b[0] == 2:
            winner = a
        elif b[0] == 3:
            if a[0] < b[0]:
                winner = a
            else:
                winner = b
    return winner

def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    print(left, right)
    return RSP(left, right)

    # def merge(left, right):
    #     result = []
    #     while len(left) > 0 and len(right) > 0:
    #         if left[0] == right[0]:
    #             result.append(left.pop(0))
    #             break
    #         if left[0] == 1:
    #             if right[0] == 2:
    #                 result.append(right.pop(0))
    #                 break
    #             elif right[0] == 3:
    #                 result.append(left.pop(0))
    #                 break
    #         if left[0] == 2:
    #             if right[0] == 1:
    #                 result.append(left.pop(0))
    #                 break
    #             elif right[0] == 3:
    #                 result.append(right.pop(0))
    #                 break
    #         if left[0] == 3:
    #             if right[0] == 1:
    #                 result.append(left.pop(0))
    #                 break
    #             elif right[0] == 2:
    #                 result.append(left.pop(0))
    #                 break
    #    return result

res = ''
T = int(input())
for i in range(1, T + 1):
    N = int(input())
    M = list(map(int, input().split()))
    res = merge_sort(M)
    print(res)