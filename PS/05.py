# codewars - Credit Card Mask
def maskify(cc):
    if len(cc) < 5:
        return cc
    else:
        l1 = l2 =  ''
        for i in range(0, len(cc)-4):
            l1 += '#'
        for i in range(len(cc)-4, len(cc)):
            l2 += cc[i]
        return l1 + l2
        
print(maskify('########SF$SDfgsd2eA'))

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]