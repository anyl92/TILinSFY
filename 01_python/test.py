a = 1
def func1():
    a = 5
    func2()

    
def func2():
    print(a, end='')

func1()
print(a)
