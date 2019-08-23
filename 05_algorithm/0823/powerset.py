# p241
# 부분집합의 길이가 3인 것의 갯수
num_list = list(range(1, 11))

def backtrack(a, k, inp):
    maxcandidates = 50
    c = [0] * maxcandidates

    if k == inp:
        print(1)
    else:
        k += 1
        ncandidate = construct_candidates(a, k, inp, c)
        for i in range(ncandidate):
            a[k] = c[i]
            backtrack(a, k, inp)

def construct_candidates(a, k, inp, c):
    c[0] = True
    c[1] = False
    return 2

NMAX = 100
a = [0]*NMAX
backtrack(num_list, 0, 3)