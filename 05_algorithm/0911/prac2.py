N = '01D06079861D79F99F'

num = [0] * 4
not_num = ['A', 'B', 'C', 'D', 'E', 'F']
ord_li = []
bin_res = ''
for i in not_num:
    n = 10
    ord_li.append(ord(i) - ord('A')+n)

for i in N:
    if i not in not_num:
        n = int(i)
    else:
        n = ord_li[not_num.index(i)]
    bin_li = [0, 0, 0, 0]
    for j in range(4):
        if n % 2 == 0:
            n //= 2
            continue
        bin_li[j] = n % 2
        n //= 2
    bin_li.reverse()
    for k in bin_li:
        bin_res += str(k)
print(bin_res)

num_li = [0]*8
total = [0]*11
for i in range(len(bin_res)//7+1):
    temp = 0
    num = bin_res[i*7:(i+1)*7]
    while len(num) != 7:
        num = '0' + num
    print(num)
    for k in range(len(num)):
        num_li[k] = num[k]
    num_li = list(map(int, num_li))
    num_li.reverse()
    for j in range(6, -1, -1):
        temp += num_li[j] * 2 ** j
        print(temp)
    total[i] = temp
print(total)
