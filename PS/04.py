# x의 n거듭제곱 구하기 == x ** n

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(2, 3))