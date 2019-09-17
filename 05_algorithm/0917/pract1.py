A = [2, 1, 4 ,3, 7, 9, 6, 5, 10, 20, 8, 0]

# def SelectionSort(A):
#     n = len(A)
#     for i in range(0, n-1):
#         min = i
#         for j in range(i+1, n):
#             if A[j] < A[min]:
#                 min = j
#         A[min], A[i] = A[i], A[min]

k = 0
def re(k):
    n = len(A)
    if k == n:
        return 1
    else:
        min = k
        for j in range(k+1, n):
            if A[j] < A[min]:
                min = j
        A[min], A[k] = A[k], A[min]
        return re(k+1)
re(k)
print(A)