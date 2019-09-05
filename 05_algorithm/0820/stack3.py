#197p
a = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
# a = [[1, 2], [1, 6], [3, 2], [5, 2], [3, 4], [5, 4], [4, 7], [7, 6]]
v = [0]* 7
stack = []
visited = []
x = 1
y = 0

stack.append(a[0][0])
stack.append(a[0][1])
visited.append(a[0][0])
visited.append(a[0][1])

while y < 2:
    while x < len(a):
        if stack[-1] == a[x][y]:
            y = int(not y)
            if a[x][y] in visited:
                y = int(not y)
                x += 1
                continue
            stack.append(a[x][y])
            visited.append(a[x][y])
            y = int(not y)
        x += 1
    x = 0
    y += 1

tmp = stack.pop()  # 3
while len(visited) < 7:
    for i in range(len(a)):
        for j in range(2):
            if a[i][j] == stack[-1]:  # 7
                j = int(not j)
                if a[i][j] not in visited:  # 5
                    stack.append(a[i][j])
                    visited.append(a[i][j])
                    j = int(not j)
                elif a[i][j] in visited:  # 6
                    if i == len(a)-1:
                        tmp = stack.pop()
                        i = 0
                        break
                    j = int(not j)
                    continue
print(visited)
