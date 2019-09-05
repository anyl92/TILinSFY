import sys
sys.stdin = open('input.txt', 'r')

def find(l):
    arr = [[0] * (total_nodes + 1) for _ in range(total_nodes + 1)]
    for i in range(total_paths):
        arr[l[i * 2]][l[i * 2 + 1]] += 1

    prior = [0] * (total_nodes + 1)
    for i in range(total_paths):
        prior[l[i * 2 + 1]] += 1

    q = []
    v = [0] * (total_nodes + 1)

    front = rear = -1

    for i in range(1, total_nodes + 1):
        if prior[i] == 0:
            q.append(i)
            rear += 1
            v[i] = 1

    while front != rear:
        front += 1
        curr = q[front]

        for k in range(total_nodes + 1):
            if arr[curr][k] == 1:
                prior[k] -= 1

        for j in range(total_nodes + 1):
            # TODO  priority check
            if arr[curr][j] == 1 and not v[j] and not prior[j]:
                q.append(j)
                rear += 1
                v[j] = 1
                prior[j] -= 1
    return (' '.join(map(str, q)))


T = 10
for t in range(T):
    total_nodes, total_paths = map(int, input().split())
    l = list(map(int, input().split()))
    print("#{} {}".format(t + 1, find(l)))