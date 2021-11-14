import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from  matplotlib import font_manager
import time
import  os

# 한글글꼴로 변경
plt.rcParams['font.size'] = 12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)


# bmi_data = pd.read_csv('./data/bmi.csv', encoding='utf-8')
# table = pd.read_html('https://www.seoul.go.kr/coronaV/coronaStatus.do')[0]
table = pd.read_html('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=', encoding='utf-8')[-1]
df = table.drop([table.index[0], table.index[-1]] ) #합계제외
df[('확진환자 (명)', '발생률 (*)')] =  df[('확진환자 (명)', '발생률 (*)')].astype(float)

# df.plot.bar()
df.plot.bar( x=('시도명','시도명'), y=[('확진환자 (명)','확진환자'), ('확진환자 (명)','발생률 (*)')], label=['확진환자','발생률'], stacked=True)
# df.plot.bar(  label=['확진환자','발생률'])
plt.title('코로나  시도별 현황')
plt.xlabel('시도명')
plt.ylabel('확진환자/발생률(명/%)')
plt.tight_layout()
plt.show()
