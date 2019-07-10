lunches = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887'
}

with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    # for lunch in lunches:
        # print(lunch, ", ", lunches[lunch])
    # for k, v in lunches.items():
    #     print(k, v)
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')
