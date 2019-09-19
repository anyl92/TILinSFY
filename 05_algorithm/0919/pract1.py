A = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]

def quick(A, l, r):
    if l < r:
        s = partitionH(A, l, r)
        quick(A, l, s-1)
        quick(A, s+1, r)

def partitionH(A, l, r):
    p = l
    i, j = l, r

    while i < j:
        while i < r and A[i] <= A[p]:
            i += 1
        while j > l and A[j] >= A[p]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[p], A[j] = A[j], A[p]
    return j

def partitionL(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

quick(A, 0, len(A)-1)
print(A)