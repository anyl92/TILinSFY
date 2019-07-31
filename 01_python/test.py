def my_sum(*args):
    for e in args:
        if type(e) not in (int, float):
            return 'fail'
    return sum(args)

print(my_sum(1, 2, 'a'))