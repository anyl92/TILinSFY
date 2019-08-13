def find():
    maxl = 0
    for i in range(N):
        num = [int(v[i])]
        card[num] = card[num] + 1
        if card[maxl] <= card[num]:
            maxl=max(maxl, num)
    return maxl