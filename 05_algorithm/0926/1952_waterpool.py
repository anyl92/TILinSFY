import sys
sys.stdin = open('input.txt', 'r')

def dfs(s, res):
    global mini
    if s > 11:
        if res < mini:
            mini = res
        return

    if plan[s]:
        if res + cost[0]*plan[s] < mini:
            dfs(s+1, res + cost[0]*plan[s])
        if res + cost[1] < mini:
            dfs(s+1, res + cost[1])
        if res + cost[2] < mini:
            dfs(s+3, res + cost[2])
    else:
        dfs(s+1, res)


T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    mini = cost[3]

    dfs(0, 0)
    print('#%d %d' % (tc, mini))