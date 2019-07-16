list_odd = []

for number in range(1, 51):
    if number % 2 == 1:
        list_odd.append(number)

print(list_odd)

list_odd = list(range(1, 50, 2))
print(list_odd)
