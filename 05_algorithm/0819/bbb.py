s = 'Reverse this strings'
#s = s[::-1]
print(s)

rev = []
for i in range(len(s)-1, -1, -1):
    rev.append(s[i])
print(''.join(rev))

l = []
slice = []
ordlist = [0]* 4
print(ord('9'))
nine = '9'
plus = 1230

# for i in range(len(nine)-1, -1, -1):
#     if nine[i] >= ord('0') and nine[i] <= ord('9'):
#         digit = nine[i] - ord('0')
#     else:
#         break
#     value = (value * 10) + digit

while plus != 0:
    slice.append(plus % 10)
    plus //= 10

for i in range(len(ordlist)):
    res = slice.pop()
    ordlist[i] = ord(str(res))

print(slice, ordlist)