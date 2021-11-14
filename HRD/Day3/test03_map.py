import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from  matplotlib import font_manager
import datetime
import time
import  os

# 한글글꼴로 변경
plt.rcParams['font.size'] = 12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

table = pd.read_html('https://www.seoul.go.kr/coronaV/coronaStatus.do')[0]


status_list = [
    ('종로구', '2320'), ('중구', '2289'), ('용산구','3352'), ('성동구', '3573'), ('광진구', '4313'),
    ('동대문구', '5069'), ('중랑구', '3573'), ('성북구', '5189'), ('강북구', '3655'), ('도봉구', '3520'),
    ('노원구', '5320'), ('은평구', '5547'), ('서대문구', '3431'), ('마포구', '4605'), ('양천구', '4223') ,
    ('강서구', '5764'), ('구로구', '6491'), ('금천구', '3154'), ('영등포구', '6200'), ('동작구', '5143'),
    ('관악구', '6938'), ('서초구', '5132'), ('강남구', '8314'), ('송파구', '8128'), ('강동구', '5336'),
    ('기타', '9070')
]

df = pd.DataFrame(status_list, columns=['구','확진자수'])
df['확진자수'] = df['확진자수'].astype('int')

print(df)
print('=' * 100)
print(datetime.datetime.now())