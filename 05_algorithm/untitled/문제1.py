T = int(input())

for tc in range(1, T+1):

    N = int(input())

    roads = [list(map(int, input().split())) for _ in range(N)]
    min_result = 10000000000000000000000
    min_high = 100000000000
    for length in range(1, 6):
        for i in range(N):
            garo = 0
            for j in range(N):
                garo += abs(length-roads[i][j])

            for j in range(N):
                sero = 0
                for top in range(0, i):
                    sero += abs(length-roads[top][j])

                for bottom in range(i+1, N):
                    sero += abs(length-roads[bottom][j])

                middle = garo+sero
                if middle < min_result:
                    min_result = middle
                    min_high = length
                elif middle == min_result:
                    if length < min_high:
                        min_high = length

    print('#{} {} {}'.format(tc, min_result, min_high))







