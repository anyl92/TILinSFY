arr = [1, 5, -9, 6, -2, -1, 2, 3, 4, -5]

subres = 0
for i in range(1, 1 << len(arr)):
    subset = []
    subres = 0
    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
    for n in range(len(subset)):
        subres += subset[n]
    if subres == 0:
        print(subset)

# n = len(arr)
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()

# for i in range(1, 1 << len(arr)):
#     subset = []
#     for j in range(len(arr)):
#         if i & (1 << j):
#             subset.append(arr[j])
#     print(subset)