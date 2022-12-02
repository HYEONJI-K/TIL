num1 = 8
num2 = 4
denum1 = 6
denum2 = 2

# 최소공배수
# num1*num2까지 반복
# num1와 num2 배수 중 공통 부분을 찾기 위해 둘 중 큰 수에 도달할 때까지 for문 돎
# 모두 값이 떨어지는 나머지가 없으면 i는 num1와num2의 최소공배수
for i in range(max(num1,num2), (num1*num2)+1):
    if i % num1 == 0 and i % num2 == 0:
        print("최소공배수 : ", i)
        break

# 최대공약수
for j in range(min(num1,num2), 0, -1):
    if num1 % j == 0 and num2 % j == 0:
        print("최대공약수 : ", j)
        break

n1 = int(i / num1)
print("n1 : ", n1)
n2 = int(i / num2)
print("n2 : ", n2)
d1 = n1 * denum1
print("d1 : ", d1)
d2 = n2 * denum2
print("d2 : ", d2)
tot = d1 + d2
print("tot : ", tot)
divi = tot % i
print("divi : ", divi)
# 약분이 필요할 경우
if tot % i == 0:
    print("--------------")
    tot = int(tot / i)
    i = int(i / i)
elif tot % divi == 0 and i % divi == 0:
    print("**************")
    tot = int(tot/divi)
    i = int(i/divi)
answer = [tot, i]
print(answer)

"""
# fractions 라이브러리를 통해 구현 가능
# 분자 : 변수이름.numerator
# 분모 : 변수이름.denominator
# 분자와 분모 추출후 answer에 append()

import fractions
def solution(denum1, num1, denum2, num2):
    answer = []
    solution = 0
    bunsu1 = fractions.Fraction(denum1, num1)
    bunsu2 = fractions.Fraction(denum2, num2)
    solution = bunsu1 + bunsu2
    answer.append(solution.numerator)
    answer.append(solution.denominator)

    return answer
'''    
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]
'''
"""
