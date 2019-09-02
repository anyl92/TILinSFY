from collections import deque

d = [69, 10, 30, 2, 16, 8, 31, 22]

def merge_sort(m):
    if len(m) < 2:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(
        else:left.pop(0))
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

print(merge_sort(d))