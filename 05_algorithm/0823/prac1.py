# p218
sic = '2+3*4/5'
stack = []
result = ''
num_list = list(map(str, range(1, 10)))
isp_0 = ['(', ')']
isp_1 = ['+', '-']
isp_2 = ['*', '/']

j = 0
for i in sic:
    if i in num_list:
        result += i
    elif i == isp_0[0]:
        stack.append(i)
    elif i == isp_0[1]:
        while stack[-1] != isp_0[0]:
            result += stack.pop()
    elif i in isp_1:  # +-
        if stack == []:
            stack.append(i)
        elif stack[-1] in isp_0:
            stack.append(i)
        else:
            result += stack.pop()
    elif i in isp_2:  # */
        if stack == []:
            stack.append(i)
        elif not stack[-1] in isp_2:
            stack.append(i)
        else:
            result += stack.pop()
            stack.append(i)
while stack != []:
    result += stack.pop()

print(result)


