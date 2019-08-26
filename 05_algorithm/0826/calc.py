import sys
sys.stdin = open('calc_input.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    N = list(map(str, input().split()))
    print(N)