
#str_a = '()()((( )))'
str_a = '((()((((()()((()())((())))))'
s = []
top = -1
for i in str_a:
    j = ord('(')
    if '(' == i:
        s.append(i)
        top +=1
        print(s)
    elif ')' == i:
        s.pop()
        top -= 1
        print(s)
print(top)