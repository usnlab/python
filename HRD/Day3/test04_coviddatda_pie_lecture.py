
import numpy as np
#from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc
import seaborn as sns
import time
import os

# 한글글꼴로 변경
plt.rcParams['font.size'] = 12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# bmi_data = pd.read_csv('./data/bmi.csv', encoding='utf-8')
table = pd.read_html('https://www.seoul.go.kr/coronaV/coronaStatus.do')[0]
df = pd.DataFrame(list(table.iloc[0]) + list(table.iloc[3]), index=list(table.columns) + list(table.iloc[2]), columns=['확진자수'])
df =  df.astype(int)
print(df) #데이터확인

# bar()형태그래프 차트 제일쉬어요
# df.plot.bar()
# plt.title('2020-11-13-코로나확진자현황')
# plt.xlabel('지역구')
# plt.ylabel('확진자수')
# plt.tight_layout()
# plt.show()

etc = df.loc['기타']
df.drop('기타', inplace=True)
df = df.append(etc)
count = df.size

#~~dict(width=0.5, edgecolor='w'), labels=df.index[:count], startangle=90, counterclock=False, autopct='', pctdistance=0.7)
_, _ , autopct = plt.pie(df['확진자수'][:count], radius=1, wedgeprops=dict(width=0.5, edgecolor='w'), labels=df.index[:count], startangle=90, counterclock=False, autopct='', pctdistance=0.7)

for i in range(count):
    autopct[i].set_text('{:,}'.format(df['확진자수'][i]))


plt.title('서울시 코로나 확진자 현황')
plt.xlabel('단위명')
plt.show()


# autopct는 부채꼴 안에 표시될 숫자의 형식을 지정합니다.  퍼센트를 표시합니다.
# startangle는 부채꼴이 그려지는 시작 각도를 설정합니다.x축에서 반시계 방향으로의 시작 각도를 설정합니다.
# counterclock=False로 설정하면 시계 방향 순서로 부채꼴 영역이 표시됩니다.
# wedgeprops웨지기본속성 : dict, default None wedgeprops=dict(edgecolor='black',linewidth=3,linestyle=':')
# wedgeprops 웨지속성 딕셔너리의 ‘width’, ‘edgecolor’, ‘linewidth’ 키를 이용해서 각각 부채꼴 영역의 너비 (반지름에 대한 비율),
# pctdistance 퍼센트를 표시할 위치를 지정할 수 있습니다. 중앙에서의 거리이며 디폴트는 0.6입니다
