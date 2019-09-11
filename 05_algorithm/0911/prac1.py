N = '0000000111100000011000000111100110000110000111100111100111111001100111'

num_li = [0]*7
total = [0]*10
temp = 0
for i in range(len(N)//7):
    temp = 0
    num = N[i*7:7*(i+1)]
    for k in range(len(num)):
        num_li[k] = num[k]
    num_li = list(map(int, num_li))
    num_li.reverse()
    for j in range(6, -1, -1):
        temp += num_li[j] * 2**j
    total[i] = temp
print(total)
