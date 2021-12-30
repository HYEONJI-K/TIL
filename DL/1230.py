# conda install plotly
# 차원을 하나 제외하고 3차원 공간에 데이터 분포를 그림
import plotly.express as px

df = px.data.iris()
# petal_length를 제외하여 3차원 공간 구성
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.show(renderer='browser')
