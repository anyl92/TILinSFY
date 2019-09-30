import sys
sys.stdin = open('2798_input.txt', 'r')

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
print(L)

L.sort(reverse=True)
print(L)

comp = {}

for i in range(1, len(L)-1):
    if L[i][0] > L[i+1][0]:
        if L[i][1] > L[i+1][1]:

