import sys
sys.stdin = open('input.txt', 'r')

def find_start(graph):
    start_pts = []
    not_start = []
    for point1 in graph:
        if point1[0] not in not_start:
            for point2 in graph:
                if point1[0] == point2[1]:
                    not_start.append(point1[0])
                    break
            else:
                start_pts.append(point1)
    return start_pts

T = 10
for t in range(1, T + 1):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = [temp[i:i + 2] for i in range(0, len(temp), 2)]
    path = []
    visited = [i for i in range(1, V + 1)]

    while graph:
        start_pts = find_start(graph)
        for point in graph:
            if point in start_pts:
                temp_pt = graph.pop(graph.index(point))
                if temp_pt[0] not in path:
                    path.append(visited.pop((visited.index(temp_pt[0]))))

    path += visited
    path = ' '.join(list(map(str, path)))

    print('#{} {}'.format(t, path))