import sys
sys.stdin = open('input.txt', 'r')

garo, sero = map(int, input().split())
cut = int(input())
L = [list(map(int, input().split())) for _ in range(cut)]

y = [0]
x = [0]
for k in range(cut):
    if L[k][0] == 1: # sero
        y.append(L[k][1])
    elif L[k][0] == 0: # garo
        x.append(L[k][1])
y.append(garo)
x.append(sero)

for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
for i in range(len(y)):
    for j in range(i+1, len(y)):
        if y[i] > y[j]:
            y[i], y[j] = y[j], y[i]

comp = []
for i in range(1, len(y)):
    for j in range(1, len(x)):
        tmp = (y[i]-y[i-1]) * (x[j]-x[j-1])
        comp.append(tmp)
        tmp = 0
print(max(comp))