from random import shuffle

def make_manito(*args):

    for i in range(len(args)):
        if args[i] == args[-1]:
            print(f'{args[i]} => {args[0]}')
        else:
            print(f'{args[i]} => {args[i+1]}')

print(make_manito('a', 'b', 'c', 'd', 'e'))  # a=>c, d=>a, b=>d ...