# codewars - String incrementer

def increment_string(strng):
    f = False
    numslice = strslice = slicenum = strsum = ''
    li = list(strng)
    number = list(map(str, list(range(0,10))))

    for i in strng:
        for j in number:
            if i == j:
                slicenum = strng.index(i)
                f = True
            if f:
                break
        if f:
            break
    
    if slicenum:
        numslice = strng[slicenum:]  # 001
        strslice += strng[:slicenum]
        strsum += str(int(numslice)+1)  # 2
        while len(numslice) != len(strsum):
            strsum = '0' + strsum
            #if len(strslice) == len(numslice):
        return strslice
    else:
        return strng+'1'

#print(increment_string("foo")) # "foo1"
print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar099")) # "foobar100"