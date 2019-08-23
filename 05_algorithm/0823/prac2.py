# p246

def backtrack(a, k, inp):
    c = [0] * 50
    res = 0
    if k == inp:
        for i in range(k+1):
            res += c[k]
        return res
    else:
        k += 1
        ncandidates = construct_candidates(a, k, inp, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, inp)

def construct_candidates(a, k, inp, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 50
a = list(range(1, 11))
backtrack(a, 0, 3)