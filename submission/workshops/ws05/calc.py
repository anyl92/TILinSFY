def my_sum(a, b):
    return a + b

def my_minus(a, b):
    return a - b

def my_multi(a, b):
    return a * b

def my_divi(a, b):
    try:
        rdivi = a / b
        if not rdivi - int(rdivi):
            rdivi = int(a/b)
        return rdivi
        
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'

# 만약 정확하게 이 파일을 실행 했을 때만, 실행 되면 좋겠다.

if __name__ == '__main__' :
    print(my_sum(1, 2))
    print(my_divi(1, 0))
