import sys
sys.stdin = open('input.txt', 'r')

garo, sero = map(int, input().split())
P = int(input())
L = [list(map(int, input().split())) for _ in range(P)]
I = list(map(int, input().split()))

int_sum = 0
for i in range(P):
    if L[i][0] == I[0]:
        int_sum += abs(L[i][1] - I[1])
    elif L[i][0]+I[0] == 3:
        tmp = L[i][1] + I[1]
        if tmp > garo*2-tmp:
            int_sum += garo*2-tmp+sero
        else:
            int_sum += tmp+sero
    elif L[i][0]+I[0] == 7:
        tmp = L[i][1] + I[1]
        if tmp > sero*2-tmp:
            int_sum += sero*2-tmp+garo
        else:
            int_sum += tmp+garo
    else:
        if I[0] == 1:
            if L[i][0] == 3:
                int_sum += I[1]+L[i][1]
            elif L[i][0] == 4:
                int_sum += garo-I[1]+L[i][1]
        elif I[0] == 2:
            if L[i][0] == 3:
                int_sum += I[1]+sero-L[i][1]
            elif L[i][0] == 4:
                int_sum += garo-I[1]+sero-L[i][1]
        elif I[0] == 3:
            if L[i][0] == 1:
                int_sum += I[1]+L[i][1]
            elif L[i][0] == 2:
                int_sum += sero-I[1]+L[i][1]
        elif I[0] == 4:
            if L[i][0] == 1:
                int_sum += I[1]+sero-L[i][1]
            elif L[i][0] == 2:
                int_sum += sero-I[1]+sero-L[i][1]
print(int_sum)








# xn, yn = map(int, input().split())
# n = int(input())
#
# store = [0] * n
# for i in range(n):
#     store[i] = list(map(int, input().split()))
# car = list(map(int, input().split()))
#
# # 1 북쪽, 2 남쪽, 3 동쪽, 4 서쪽
# # 숫자가 같은 같은 변에 있는 경우 ==> 차이의 절대값
# # 4개에서 2개 뽑는 경우 6가지
# # 1, 2 또는 3, 4 평행 ==> 더해서 최소값 또는 최대값 인 경우 평행
# # 나머지 4가지 경우는 변이 맞닿아 있는 경우
#
# sum = 0
# for i in range(n):
#     if store[i][0] == car[0]:
#         sum += abs(store[i][1] - car[1])
#     elif store[i][0] + car[0] == 3:
#         if store[i][1] + car[1] < xn:
#             sum += (yn + store[i][1] + car[1])
#         else:
#             sum += (yn + 2 * xn - store[i][1] - car[1])
#     elif store[i][0] + car[0] == 7:
#         if store[i][1] + car[1] < yn:
#             sum += (xn + store[i][1] + car[1])
#         else:
#             sum += (xn + 2 * yn - store[i][1] - car[1])
#     else:
#         if store[i][0] == 1:
#             if car[0] == 3:
#                 sum += (store[i][1] + car[1])
#             elif car[0] == 4:
#                 sum += (xn - store[i][1] + car[1])
#         elif store[i][0] == 2:
#             if car[0] == 3:
#                 sum += (store[i][1] + yn - car[1])
#             elif car[0] == 4:
#                 sum += (xn - store[i][1] + yn - car[1])
#         elif store[i][0] == 3:
#             if car[0] == 1:
#                 sum += (store[i][1] + car[1])
#             elif car[0] == 2:
#                 sum += (yn - store[i][1] + car[1])
#         elif store[i][0] == 4:
#             if car[0] == 1:
#                 sum += (store[i][1] + xn - car[1])
#             elif car[0] == 2:
#                 sum += (yn - store[i][1] + xn - car[1])
#
# print(sum)
