#양의 정수 x 입력받아 근사값을 반환하는 함수작성
#sqrt() 사용금지
#x = input('양의 정수:')

#루트3은 0과1사이가 아니라 1과2사이에있다 - 제곱한다
#1과1.5사이 또는 1.5와2사이 - 그럼 1.5와2사이가됨- 제곱한다
#1.5와 1.75사이 또는 1.75와 2사이 - 그럼 ?가 됨 - 제곱한다

import math

# def bis(n, mini=0, maxi=1):
#     if maxi ** 2 == n:
#         return maxi
#     elif mini ** 2 == n:
#         return mini
#     elif math.isclose(mini, maxi):
#         return mini
    
#     if mini ** 2 < n < maxi ** 2 :
#         guess = (mini + maxi) / 2
#         if guess ** 2 < n:
#             return bis(n, guess, maxi)
#         else:
#             return bis(n, mini, guess)
#     else:
#         mini, maxi = maxi, maxi+1
#         return bis(n, mini, maxi)
        
# print(bis(3))

def bis(n, mini = 0, maxi = 1):
    while not math.isclose(mini, maxi):
        if maxi ** 2 == n:
            return maxi
        elif mini ** 2 == n:
            return mini
        elif mini ** 2 < n < maxi ** 2:
            guess = (mini + maxi) / 2
            if guess ** 2 < n:
                mini = guess
            else:
                maxi = guess
        else:
            mini, maxi = maxi, maxi + 1
    return mini
print(bis(3))