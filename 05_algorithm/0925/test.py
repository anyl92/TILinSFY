def sol(count, info_list, info_int, visited):
    global max_info
    if count == num_int:
        if max_info < info_int:
            max_info = info_int
        return
    else:
        for k in range(len(info_list)):
            for i in range(len(info_list)):
                if k != i:
                    info_list[k], info_list[i] = info_list[i], info_list[k]
                    info_int = int(''.join(info_list))
                    if count != num_int - 1:
                        if not visited[info_int]:
                            visited[info_int] = 1
                            count += 1
                            sol(count, info_list, info_int, visited)
                            count -= 1
                        info_list[k], info_list[i] = info_list[i], info_list[k]
                    else:
                        count += 1
                        sol(count, info_list, info_int, visited)
                        count -= 1
                        info_list[k], info_list[i] = info_list[i], info_list[k]


T = int(input())
for tc in range(1, T + 1):
    info, num = input().split()  # 123, 1
    num_int = int(num)
    info_list = list(info)
    info_int = int(''.join(info_list))
    max_info = 0
    visited = [0] * 1000000
    visited[info_int] = 1
    sol(0, info_list, info_int, visited)
    print('#{} {}'.format(tc, max_info))