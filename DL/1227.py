"""
import 명령어 '모듈을 불러와 쓸 수 있게 해준다'
# 모듈에 정의되어 있는 변수, 함수, 클래스를 프로그램에 포함시켜 '모듈.변수' '모듈.함수' '모듈.클래스' 형태로 쓸 수 있다.
# 연산자 오버로딩 : 하나의 연산자가 피연산자에 따라 서로 다른 기능을 하는 특성

클라우드 방식
# 프로그램과 데이터가 서버에 저장되고 관리
# 서버에 환경이 대부분 갖추어져 있어 로그인하면 바로 프로그래밍 가능
# 인터넷 연결만 있으면 어느 곳에서나 개발 / 협업 가능

스탠드얼론 방식
# 자신에 최적인 환경 구축 가능
# 프로그램과 데이터가 자신의 컴퓨터에 저장
# 소프트웨어를 설치하고 환경을 스스로 구축
"""

import random
a = random.randint(10, 20)
b = random.randint(10, 20)

c = a + b
print(a,b,c)
# 15 17 32

"""
아나콘다 프롬프트 가상 환경 만들기
(base) C:/> conda create -n aip python=3.9    # aip 가상 환경 생성
(base) C:/> conda activate aip                # aip 가상 환경으로 이동
(base) C:/> conda install spyder              # aip 가상 환경에 스파이더 설치
(base) C:/> conda install tensorflow          # aip 가상 환경에 텐서플로 설치
"""
