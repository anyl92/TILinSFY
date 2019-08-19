import sys
sys.stdin = open('sample_input.txt')

def search_text(testing_text, searching_text):
    idx = 0
    test = []
    search = []
    for i in testing_text:
        test.append(i)
    for i in searching_text:
        search.append(i)
    for i in range(len(test)-len(search)):
        if test[i:i+len(search)] == search:
            idx = i
            result = 1
            break
        else:
            result = 0
    return result

test_case = int(input())
for numbers in range(1, test_case + 1):
    searching_text = input()
    testing_text = input()
    result = search_text(testing_text, searching_text)
    print('#{} {}'.format(numbers, result))