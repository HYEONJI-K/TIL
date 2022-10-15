from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score
import numpy as np

"""
cross_val_score 함수가 교차 검증 수행 (cv=5는 5-겹 교차 검증)
"""

digit = datasets.load_digits()
s = svm.SVC(gamma=0.001)
# 5-겹 교차 검증
accuracies = cross_val_score(s,digit.data, digit.target, cv=5)

print(accuracies)
print("정확률(평균)=%0.3f, 표준편차=%0.3f"%(accuracies.mean()*100,accuracies.std()))

"""
[0.975      0.95       0.98328691 0.99164345 0.96100279]
정확률(평균)=97.219, 표준편차=0.015

실행 결과 정확률이 들쭉날쭉. 한번만 시도하는 1231_1.py의 위험성을 보여줌
k를 크게 하면 신뢰도는 높아지지만 실행 시간이 더 걸림
"""