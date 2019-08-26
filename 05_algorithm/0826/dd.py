def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    sum = 0
    for i in range(1, 11):
        if a[i] == True:
            sum += i
    if sum == 10:
        for i in range(1, 11):
            if a[i] == True:
                print(i, end=' ')
        print()

def backtrack(a, k, input):
    c = [0]

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]