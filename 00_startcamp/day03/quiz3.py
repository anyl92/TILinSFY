number = int(input('숫자를 입력하세요: '))

# if number % 2 == 0:
#     print('짝수입니다.')
# else:
#     print('홀수입니다.')


# fizz buzz => 3배수 fizz / 5배수 buzz / 15배수 fizzbuzz

for i in range(1, number+1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
