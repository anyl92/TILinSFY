import sys
sys.stdin = open('sample_input.txt', 'r')

def Card(N, num):
    numbers = {}
    for i in num:
        numbers[i] = num.count(i)
    count = max(numbers.values())
    key = 0
    for j in numbers.keys():
        if numbers[j] == count:
            if key < j:
                key = j
    return ("#%d %s %d" % (tc, key, count))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    res = Card(N, num)
    print(res)