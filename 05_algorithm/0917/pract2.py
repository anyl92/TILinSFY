
def perm(n, k):
    global res
    if k == n:
        for i in range(0, len(arr), 3):
            if int(arr[i]) + 2 == int(arr[i + 1]) + 1 == int(arr[i + 2]):
                continue
            elif int(arr[i]) == int(arr[i + 1]) == int(arr[i + 2]):
                continue
            else:
                return
        res = 'Babygin'
        return
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]
        print(arr)

arr = list('667767')
res = 'False'
perm(len(arr), 0)
print(res)