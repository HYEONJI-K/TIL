import time

start = time.time()
sum = 0

for i in range(1, 100000001):
    sum = sum + 1

end = time.time()

print('1 + ... + 100000000 = ', sum)
print('소요 시간은 ', end, '초입니다.')

"""
1 + ... + 100000000 =  100000000
소요 시간은  1640675042.370306 초입니다.
"""
'''
================================================================
'''

from datetime import datetime

# 경기 결과 입력
p = input('place : ')
t = input('time : ')
o = input('other team : ')
g = input('son\'s goal : ')
a = input('any help : ')
s_m = input('son\'s team goal : ')
s_y = input('other team goal : ')

# 기사 작성
news = "[프리미어 리그 속보("+str(datetime.now())+")]\n"
news = news + "Son"+p+t+"출전"
news = news + "Other team is "+o

if s_m > s_y:
    news = news+"Son's team"+s_m+"Other team"+s_y+"Son's team win!"
elif s_m < s_y:
    news = news+"Son's team"+s_m+"Other team"+s_y+"Son's team lose!"
else:
    news=news+"비김"

if int(g)>0 and int(a)>0:
    news=news+"Son"+g+a
elif int(g)>0 and int(a)==0:
    news=news+"Son"+g
elif int(g)==0 and int(a)>0:
    news=news+"Son"+a
else:
    news=news+a+"침묵을 지켰다."
    
print(news)

'''
# 입력
place : Seoul

time : 12.28.2021

other team : Park

son's goal : 1

any help : 3

son's team goal : 4

other team goal : 6

# 출력
[프리미어 리그 속보(2021-12-28 16:15:11.857435)]
SonSeoul12.28.2021출전Other team is ParkSon's team4Other team6Son's team lose!Son13
'''

"""
wording = ["상대 팀을 이겼습니다.", "상대를 대상으로 통쾌한 승리를 거머쥐었습니다.", "상대 팀을 꺾었습니다.
news = news + random.choice(wording)
문장을 랜덤 선택하여 단조로움 해소
* 자연어 처리 기술과 word2vec과 같은 언어 모델 활
"""
