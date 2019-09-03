import sys
sys.stdin = open('input.txt', 'r')

# def check(i):
#     num_li = []
#     n = i
#     for _ in range(len(str(i))):
#         num_li += [i % 10]
#         i //= 10
#     for j in range(len(num_li)):
#         for k in range(1 + j, len(num_li)):
#             if num_li[j] < num_li[k]:
#                 return False
#     return n

def check(i):
    n, i = i, str(i)
    for j in range(1, len(i)):
        if i[j-1] > i[j]:
            return False
    return n

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))

    result = []
    mul_li = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            mul_li = L[i] * L[j]
            if check(mul_li):
                result += [check(mul_li)]
    if result == []:
        print('#%d' % (tc), -1)
    else:
        print('#%d %d' % (tc, max(result)))