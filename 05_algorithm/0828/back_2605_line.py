import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
L = list(map(int, input().split()))
line = [0]*N
stdnum = 1
line[0] = stdnum
stdnum += 1
for i in range(1, N):
    for j in range(L[i]):
        line[i-j] = line[i-1-j]
    line[i-L[i]] = stdnum
    stdnum += 1
for i in line:
    print(i, end=' ')