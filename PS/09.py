# codewars - Sort the odd

def sort_array(source_array):
    tmp_list = []
    for i in range(len(source_array)):
        if source_array[i] == 0:
            continue
        elif source_array[i] % 2:
            tmp_list.append(source_array[i])
    print(sorted(tmp_list))  # [1, 3, 5]
    for i in tmp_list:
        for j in source_array:
            if j % 2:
                source_array.index[j]

sort_array([5, 3, 2, 8, 1, 4])  # [1, 3, 2, 8, 5, 4]