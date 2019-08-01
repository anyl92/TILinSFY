# codewars - Persistent Bugger

def persistence(n):
    length = len(str(n))
    while length > 1:
        mul = 1
        for i in range(length):
            mul *= int(str(n)[i])
        length = len(str(mul))
        n = mul
    return n
print(persistence(39))


import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

