my = [1, 2, 3, 4, 5, 6]
real = [11, 2, 3, 4, 5, 7]
bonus = 6

# my와 real의 숫자가 모두 같으면 1등
# my와 real이 5개가 같고 나머지 하나가 bonus면 2등
# my와 real이 5개가 같으면 3등
# '' 4개가 같으면 4등
# '' 3개가 같으면 5등
# 나머지는 꽝

for i in range(0, 6):
    if my[i] == real[i]:
        n = i

print(i, n)


if my == real:
    print('1등')
elif (n = 4) & 
else:
    print('꽝')
