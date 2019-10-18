import sys
sys.stdin = open('1260.txt', 'r')

N, M, V = map(int, input().split())
L = []
for _ in range(M):
    L += map(int, input().split())
print(L)

linked = [[] for _ in range(N+1)]
for i in range(len(L)//2):
    linked[L[2*i]].append(L[2*i+1])
    linked[L[2*i+1]].append(L[2*i])
print(linked)

