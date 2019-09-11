N = '0269FAC9A0'

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

pattern = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111',
]

ans = ''
l = len(bin_res)-1
while l > 0:
    if bin_res[l] == '1':
        for i in pattern:
            if i == str(bin_res[l - 5:l + 1]):
                ans += str(pattern.index(i))
                l -= 5
                break
    l -= 1
print(ans[::-1])