ary = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9],
       ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sum_list = []
sum_str = 0

for x in range(len(ary)):
    for y in range(len(ary[x])):
        for I in range(4):
            if 0 <= x + dx[I] < len(ary[x]) and 0 <= y + dy[I] < len(ary):
                a = abs(ary[x][y] - ary[x + dx[I]][y + dy[I]])
                sum_str += a
        #sum_list.append(sum_str)
        # print('yy %d' % (sum_str), end='\n')
        # sum_str = 0
print(sum_str)





# def isWall(x, y):
#     if x < 0 or x >= 5: return True
#     if y < 0 or y >= 5: return True
#     return False
#
# def calAbs(y, x):
#     if y-x > 0: return y-x
#     else: return x-y
#
# for x in range(len(ary)):
#     for y in range(len(ary[x])):
#         for I in range(4):
#             testX = x+dx[i]
#             testY = y+dy[i]
#             if isWall(testX, testY) == False:
#                 sum+= calAbs(arr[x][y], arr[testX][testY])
# print("sum= %d" %sum)
