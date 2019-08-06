# 보충 알고리즘

def find_one(*args):
    numbers = list(args)
    total = {}

    for number in numbers:
        count = numbers.count(number)
        total[number] = count
    for idx, val in total.items():
        if val % 2:
            return idx


    r = 0
    for n in args:
        r ^= n
    return r
    
    

# 숫자 set이 들어옵니다. -> 단 하나만 홀수개가 들어옵니다.
print(find_one(1, 2, 1))
print(find_one(1, 1, 2, 2, 3, 3, 3))
print(find_one(4, 3, 2, 1, 10, 1, 2, 4, 3))