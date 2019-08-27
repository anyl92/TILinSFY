import sys
sys.stdin = open('squence.txt', 'r')

N, K = map(int, input().split())
L = list(map(int, input().split()))
tmp = 0
tmp_sum = 0
for i in range(len(L)-K+1):
    for j in range(K):
        tmp_sum += L[i+j]
    if tmp < tmp_sum:
        tmp = tmp_sum
    tmp_sum = 0
print(tmp)