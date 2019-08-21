import sys
sys.stdin = open('pel_input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     K = [[char for char in input()] for n in range(N)]
#     for row in K:
#         for i in range(N-M+1):
#             row_1 = row[i:M+i+1]
#             # row_2 = list(reversed(row[i:M+i+1]))
#             if row_1 == row_1[::-1]:  # if row_1 == row_2:
#                 print('#{} {}'.format(tc, ''.join(row_1)))
#     for col in range(len(K)):
#         for l in range(N-M+1):
#             col_1 = []
#             for j in range(M):
#                 col_1.append((K[j+l][col]))
#             if col_1 == col_1[::-1]:
#                 print('#{} {}'.format(tc, ''.join(col_1)))


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    K = [[char for char in input()] for n in range(N)]
    for row in range(len(K)):
        for i in range(N-M+1):
            row_1 = K[row][i:M+i+1]
            # row_2 = list(reversed(row[i:M+i+1]))
            if row_1 == row_1[::-1]:  # if row_1 == row_2:
                print('#{} {}'.format(tc, ''.join(row_1)))
        for l in range(N-M+1):
            col_1 = []
            for j in range(M):
                col_1.append((K[j+l][row]))
            if col_1 == col_1[::-1]:
                print('#{} {}'.format(tc, ''.join(col_1)))