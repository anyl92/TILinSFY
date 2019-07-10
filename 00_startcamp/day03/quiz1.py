import random

# input()
name = input('What\'s your name? : ')
print('hi, ' + name)


words = input('입력 고고 : ')
# words의 첫 글자와 마지막 글자를 출력하라.
print(type(words))
my_list = list(words)
print(my_list)
print(words[0], words[-1])

length = random.choice(range(1, 100))
numbers = list(range(length))

numbers[length - 1]
print(numbers[length - 1])

print(numbers[-1])


numbers = [1, 2, 3, 4, 5]
# numbers의 첫 요소와 마지막 요소를 출력하라.
print(numbers[0], numbers[4])
