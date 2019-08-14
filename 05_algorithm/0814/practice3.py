ary = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14],
       ]

# for x in range(len(ary)):
#     for y in range(len(ary[x])):
#         for I in range(4):
#             if 0 <= x + dx[I] < len(ary[x]) and 0 <= y + dy[I] < len(ary):
#                 a = abs(ary[x][y] - ary[x + dx[I]][y + dy[I]])
#                 sum_str += a
# print(sum_str)

for x in range(len(ary)):
    for y in range(len(ary[x])):
        check_min = ary[x][y]
        if check_min > ary[x][y]:
            check_min = ary[x][y]
    if check_min > ary[x]