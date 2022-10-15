from sklearn import datasets
import matplotlib.pyplot as plt

"""
lfw(labeled faces in the wild) 데이터셋
- 5749명의 유명인의 얼굴 영상 13233장. 50*37맵. [0,255] 명암값
- 데이터 편향 주의(어린이, 흑인 등이 적어 얼굴 인식 프로그램을 제작하는데 부적합)
"""
# 데이터셋 읽기
lfw = datasets.fetch_lfw_people(min_faces_per_person=70, resize=0.4)

plt.figure(figsize=(20,5))

# 처음 8명을 디스플레이 
for i in range(8):
    plt.subplot(1,8,i+1)
    plt.imshow(lfw.images[i],cmap=plt.cm.bone)
    plt.title(lfw.target_names[lfw.target[i]])
    
plt.show()

"""
20newsgroups 데이터셋
- 웹에서 수집한 문서를 20개 부류로 구분. 텍스트로 구성되어 샘플의 길이가 다름
- 시계열 데이터(단어가 나타나는 순서가 중요. 8장의 순환 신경망에서 다룸)
"""

news = datasets.fetch_20newsgroups(subset='train')
print("*****\n",news.data[0],"\n*****")
print("이 문서의 부류는 <",news.target_names[news.target[0]],"> 입니다.")