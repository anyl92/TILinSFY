def func(c='5', *args):  # c == '3', args == ('4', '1', '2')
    a, c, b = args  # a '4' c '1' b '2'
    return a + b + c
print(func('3', '4', '1', '2'))


name = 'hong'
class Person:
    name = 'choi'
    def greeting(self):
        print(name)
p1=Person()
p1.name='kim'
p1.greeting()  # hong


word = 'python'
indexing = word[3:8]
print(indexing) # hon


a = 1
def func_1():
    a = 5
    func_2()

def func_2():
    print(a, end='')
func_1()
print(a)  # 11