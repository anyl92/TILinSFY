# n을 입력받고, 1부터 n까지 출력하라

n = input('자연수를 입력하세요: ')
n = int(n)  # str => int(str) 숫자일 경우 정수변환 가능
print(type(n))

i = 1
number = []

# while i <= n:
#     number.append(i)
#     i = i + 1
# print(number)

for i in range(n):
    print(i + 1, end=' ')  # print \n default
#     number.append(i + 1)
# print(number)
