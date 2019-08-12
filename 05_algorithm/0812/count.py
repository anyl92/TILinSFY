#def Counting_Sort(A, B, k)
# A [1..n] -- 입력 배열(1 to k)
# B [1..n] -- 정렬된 배열
# C [1..k] -- 카운트 배열

A = [0, 4, 1, 3, 1, 2, 4, 1]
B = sorted(A)

    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += i

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for I in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

print(Counting_Sort())