import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

#  한글글꼴로 변경
plt.rcParams['font.size'] = 12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'


font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# tips = sns.load_dataset('tips')
# print(tips)
# print('-' * 100)
# ri = np.random.randint(1,20,5)
# print(ri)

# print('-' * 100 )
# tips = sns.load_dataset('tips')
# print(tips.head())
# print(tips.tail())
# print()
# print(tips.info())
# print()

# y1 = [10, 40, 54, 25]
# y2 = [60, 30, 40]
# y3 = np.random.randint(1,15,5) 
# y4 = [30, 90, 10, 70, 55]
# fig,ax = plt.subplots(2,2) #2행2열
# ax[0,0].plot(['둘리', '또치', '희동', '도우넛'] , y1)
# ax[0,1].plot(['영희', '철수', '미미'] , y2)
# ax[1,0].plot(['aa', 'bb', 'cc', 'dd', 'ee'] , y3)
# ax[1,1].plot(['가', '나', '다', '라', '마'] , y4)
# plt.show() #show()함수는 필수입니다 


tips = sns.load_dataset('tips') #tip데이터로 여러 다양한 형태 차트그래프 조작 
ax = sns.distplot(tips['total_bill'], rug=True)
ax.set_title('전체 금액 표시하기')
ax.set_xlabel('서비스 금액')
ax.set_ylabel('빈도수')
plt.show()
print('-' * 100 )

print(tips.info())
ax = sns.barplot(x='tip', y='day', data=tips, capsize=.2)
ax.set_title('BAR 표시하기')
ax.set_xlabel('서비스 금액')
ax.set_ylabel('Day')
plt.show()

plt.figure(figsize=(10,6))
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.randn(100)
sizes = 1000*np.random.rand(100)
plt.scatter(x,y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar()
plt.show()
