# matplotlib 라이브러리응 이용한 샘플 디스플레이와 샘플 내용(화솟값) 출력
# 필기 숫자 데이터
from sklearn import datasets
import matplotlib.pyplot as plt

digit = datasets.load_digits()

plt.figure(figsize=(5,5))
# 0번 샘플을 그림
plt.imshow(digit.images[0], cmap=plt.cm.gray_r, interpolation='nearest')

plt.show()
# 0번 샘플의 화솟값을 출력
print(digit.data[0])
print("이 숫자는 ", digit.target[0],"입니다.")