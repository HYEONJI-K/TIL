import numpy as np
x2=np.array([1,0,1])    # sample
w=np.array([-0.5,1.0,1.0]) # 퍼셉트론 가중치 벡터
s=sum(x2*w) # 요소별 곱한 후 합산
print(s)

# 0.5

x = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
s2 = np.sum(x*w,axis=1)    # 샘플 각각에 대해 요소별로 곱한 후 요소를 합산
print(s2)

# [-0.5  0.5  0.5  1.5]