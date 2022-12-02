order = int(input())
answer = 0
# 입력받은 숫자 한 자리씩 나누기
for i in map(int, str(order)):
    if i != 0:
        if int(i) % 3 == 0:
            answer += 1
            print(i, " : ", answer)
    else:
        pass
print(answer)

"""
<output>

3000
3  :  1
1
"""
