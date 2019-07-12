my = [1, 2, 3, 4, 5, 6]
real = [1, 2, 3, 4, 5, 6]
bonus = 7

# my와 real의 숫자가 모두 같으면 1등
# my와 real이 5개가 같고 나머지 하나가 bonus면 2등
# my와 real이 5개가 같으면 3등
# '' 4개가 같으면 4등
# '' 3개가 같으면 5등
# 나머지는 꽝

m = 0  # 보너스 체크
count = 0  # my와 real 비교, 같은 개수 출력
i = 0
j = 0

for i in range(0, 6):
    for j in range(0, 6):
        if my[i] == real[j]:
            count += 1

for k in range(0, 6):
    if my[k] == bonus:
        l = 1
    else:
        l = 0

# 선생님의답안
# match_count = 0
# is_bonus = False
# for i in my:
#     if i == bonus:
#         is_bonus = True
#     for j in real:
#         if i == j:
#             match_count += 1

# 또는 bonus를 아래 if문에서 count==5일때만 돌림
# if bonus in my:
#     is_bonus = True | result = '2등'

# 아래if문에서
    # if is_bonus:
    #     result = '2등'
    # else:
    #     result = '3등'

if my == real:
    result = '1등'
elif (count == 5) & (l == 1):
    result = '2등'
elif count == 5:
    result = '3등'
elif count == 4:
    result = '4등'
elif count == 3:
    result = '5등'
else:
    result = '꽝'

# 다른 풀이
match = set(my).intersection(set(real))
match_count = len(match)
