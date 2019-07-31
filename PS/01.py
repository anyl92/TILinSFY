# hackerrank - Simple Array Sum

number = input('count: ')
sum_list = input().split()

def list_sum(number, sum_list):
    result = 0

    while len(sum_list) != int(number):
        print('error!')
        sum_list = input('number: ').split()
    
    for i in sum_list:
        result += int(i)
        
    return result

print(list_sum(number, sum_list))
