import sys
sys.stdin = open('2798_input.txt', 'r')

N = int(input())
num = 1

while num <= N:
    sum_num = num
    str_num = str(num)

    if num == N:
        print(0)

    for i in range(len(str_num)):
        sum_num += int(str_num[i])

    if sum_num == N:
        print(num)
        break

    num += 1


