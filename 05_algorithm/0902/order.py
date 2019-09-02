import sys
sys.stdin = open('order_input.txt', 'r')

def dfs(start):
    global result

    if len(result) == V:
        return
    visited[start] = 1
    if start not in result:
        result += [start]
        #print(result)
    for next in range(1, V+1):
        if True not in parent:
            return
        if start == next:
            continue
        elif link_cord[start][next] and parent[next] != 0 and not visited[next]:
            parent[next] -= 1
            if parent[next] == 0:
                result += [next]
                visited[next] = 1
                dfs(next)


for tc in range(3):
    result = []
    V, E = map(int, input().split())
    link_cord = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0] * (V+1)
    parent = [0] * (V+1)
    link = list(map(int, input().split()))
    #print(V, E, link)

    while len(link) != 0:
        b = link.pop()
        a = link.pop()
        link_cord[a][b] = 1
        parent[b] += 1
    for i in range(1, V+1):
        if visited[i] == 1:
            continue
        if parent[i] == 0:
            dfs(i)
    print('#%d' % (tc), end=' ')
    for i in result:
        print('%d' % (i), end=' ')
    print()