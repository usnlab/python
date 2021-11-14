
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

# path='./Day3/data/bmi.csv'
# bmi_data = pd.read_csv(path, encoding='utf-8')
# bmi_data.head()

table = pd.read_html('https://www.seoul.go.kr/coronaV/coronaStatus.do')[0]
df = pd.DataFrame(list(table.iloc[0]) + list(table.iloc[3]), index=list(table.columns) + list(table.iloc[2]), columns=['확진자수'])
df=  df.astype(int)
print(df)

#df.plot.bar(x=('district'),y=('확진자수'), label=['District','Number'],stacked=True)
df.plot.bar()
plt.title('2020-11-13 COVID STATUS')
plt.tight_layout()
plt.show()

