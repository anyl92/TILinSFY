import sys
sys.stdin = open('input.txt', 'r')

sero, garo = map(int,input().split())
L = [list(map(str, input().split())) for _ in range(sero)]
print(L)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(garo):
    if L[0][i] == 'L'
