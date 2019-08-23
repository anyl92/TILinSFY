# p243 ?????

def construct_candidates(a, k, inp, c):
    in_perm = [False] * 100

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, inp+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

def backtrack(a, k, inp):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k+1):
            print('ai', a[i])
            return a[i]
    else:
        k += 1
        ncandidates = construct_candidates(a, k, inp, c)
        for i in range(ncandidates):
            a[k] = c[i]
            print(backtrack(a, k, inp))

MAXCANDIDATES = 100
a = [0] * MAXCANDIDATES
print(backtrack(a, 0, 3))