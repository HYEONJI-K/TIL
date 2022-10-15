from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np

# 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
digit = datasets.load_digits()
# train_test_split 함수로 훈련 60%, 테스트 40%로 랜덤 분할
x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, train_size=0.6)

# svm의 분류 모델 SVC를 학습
s = svm.SVC(gamma=0.001)
# 훈련 집합 x_train, y_train을 fit 함수에 주어 학습 수행
s.fit(x_train,y_train)

# 테스트 집합의 특징 벡터 x_test를 predict 함수에 주어 예측 수행
res = s.predict(x_test)

# 혼동 행렬 구함
# 테스트 집합의 레이블 y_test를 가지고 혼동 행렬 계산
conf = np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]]+=1
print(conf)

# 정확률 측정하고 출력
no_correct = 0
for i in range(10):
    no_correct += conf[i][i]
accuracy = no_correct/len(res)
print("테스트 집합에 대한 정확률은 ",accuracy*100,"%입니다.")

"""
[[78.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0. 61.  0.  0.  0.  0.  0.  0.  2.  0.]
 [ 0.  0. 73.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0. 71.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0. 81.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0. 76.  0.  0.  0.  2.]
 [ 0.  0.  0.  0.  0.  0. 83.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0. 63.  0.  0.]
 [ 0.  1.  0.  0.  0.  0.  1.  0. 59.  1.]
 [ 0.  0.  0.  0.  0.  1.  0.  0.  0. 65.]]
테스트 집합에 대한 정확률은  98.74826147426981 %입니다.
"""

"""
난수를 사용하기 때문에 실행할 때마다 다른 결과가 나온다
동일한 실행 결과를 얻으려면?
9행 전에 np.random.seed(0)을 추가하면(매개변수 0은 변경가능) 어떤 값이든 고정시켜 매번 같은 난수 열이 생성된다.
"""