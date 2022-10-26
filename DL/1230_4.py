# 특징 추출을 위한 코드 작성
# sklearn이 제공하는 fit 함수로 모델링(학습)
# predict 함수로 예측
"""
화소 각각을 특징으로 간주
- sklearn의 필기 숫자는 8*8 맵으로 표현되므로 64차원 특징 벡터
- 2차원 구조를 1차원 구조로 변환
x = (0,0,21,34,---)

* 각 화소를 특징으로 간주하여 64차원 특징 벡터 사용
"""

from sklearn import datasets
from sklearn import svm

digit = datasets.load_digits()

# svm의 분류기 모델 SC를 학습(training)
# SVC로 학습 수행
# 특징 벡터 digit.data, 레이블 digit.target 사용
s=svm.SVC(gamma=0.1, C=10)
# digit 데이터로 모델링
s.fit(digit.data,digit.target)

# 훈련 집합의 앞에 있는 샘플 3개(테스트 집합으로 간주)를 새로운 샘플로 간주하고 인식(예측)해봄
new_d = [digit.data[0], digit.data[1], digit.data[2]]
res = s.predict(new_d)
print("예측값은 ", res)
print("참값은 ", digit.target[0], digit.target[1],digit.target[2])

# 훈련 집합을 테스트 집합으로 간주하여 인식해보고 정확률을 측정
res = s.predict(digit.data)
correct = [i for i in range(len(res)) if res[i]==digit.target[i]]
accuracy = len(correct)/len(res)
print("화소 특징을 사용했을 때 정확률 = ", accuracy*100, "%")
"""
예측값은  [0 1 2]
참값은  0 1 2
화소 특징을 사용했을 때 정확률 =  100.0 %
"""