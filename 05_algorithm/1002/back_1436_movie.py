import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
li = [0] * 10000

start = 666
index = 0
while index < 10000:
    if '666' in str(start):
        li[index] = start
        index += 1
    start += 1
print(li[N-1])