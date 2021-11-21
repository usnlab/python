import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from  matplotlib import font_manager
import datetime
import time
import  os
import json
import webbrowser
import folium

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

"""
location1 = [37.555403, 126.937188]
map = folium.Map(location1, zoom_start=14)

with open('./Day3/data/seoul_municipalities_geo.json', mode='r', encoding='utf-8') as jsfile :
    bit = json.loads(jsfile.read())
    map = folium.Map(location1, zoom_start=14)
    folium.Choropleth(geo_data=bit, 
                    data = df,
                    columns=['구','확진자수'],
                    key_on='feature.id',
                    fill_color='Purples',
                    line_color='black',
                    line_weight=1,
                    line_opacity=0.7).add_to(map)
jsfile.close()

geo_path = './Day3/data/서울시+행정구역+시군구+정보+(좌표계_+WGS1984).json'
with open(geo_path, mode='r', encoding='utf-8') as ff :
    geo_data = json.loads(ff)
    for data  in geo_data['DATA']:
        msg = '<div style="background-color:tomato;color=blue;font-size=110%;"> {}<br>{}명</div>'.format(data['sig_kor_nm'], df[df['구']==data['sig_kor_nm']]['확진자수'].tolist()[0])
        folium.Marker(
            location=[float(data['lat']),float(data['lng'])], 
            popup='HEAD',
            icon=folium.DivIcon(html=msg, icon_size=(60,60), icon_anchor=(0,0))).add_to(map)
    iframe = folium.IFrame(msg, width=120, height=100)
    popup = folium.Popup(iframe, max_width=120)
    folium.Marker(
            location=[float(data['lat']),float(data['lng'])], 
            popup=popup,
            icon=folium.Icon(color='blue', icon='star')).add_to(map)

"""

#seoul_municipalities_geo.json  ==> close()안해도 되는  with open(seoul_municipalities_geo.json  , r, 인코딩 )  as  ff 
#json형태저장 dumps,  json형태읽기 loads, 
#with open('./Day3/data/seoul_municipalities_geo.json', mode='r', encoding='utf-8') as ff :
with open('../Data/data/seoul_municipalities_geo.json', mode='r', encoding='utf-8') as ff :
    geo_data=json.loads(ff.read())
    map = folium.Map(location=[37.55262899509166, 126.93777255354891], zoom_start=12)
    folium.Choropleth( geo_data=geo_data,
                   data = df ,
                   columns=['구', '확진자수'], 
                   key_on='feature.properties.SIG_KOR_NM' ,
                   legend_name='서울시 지역별 표시',
                   line_opacity=0.5).add_to(map)


#geo_path  = './Day3/data/서울시+행정구역+시군구+정보+(좌표계_+WGS1984).json'
geo_path  = '../Data/data/서울시+행정구역+시군구+정보+(좌표계_+WGS1984).json'
with open(geo_path, mode='r', encoding='utf-8') as ff :
    geo_data = json.load(ff)
    print('geo_data ', geo_data)

    for data  in geo_data['DATA']:
        msg = '<div style="background-color:yellow;font-size=110%;"> {}<br>{}명</div>'.format(data['sig_kor_nm'], df[df['구']==data['sig_kor_nm']]['확진자수'].tolist()[0])
        folium.Marker(
            location=[float(data['lat']) , float(data['lng'])],  
            icon=folium.DivIcon(html=msg, icon_size=(60,60), icon_anchor=(0,0))).add_to(map)

    iframe = folium.IFrame(msg, width=120, height=100)
    popup = folium.Popup(iframe, max_width=120)
    folium.Marker(
            location=[float(data['lat']) , float(data['lng'])], 
            popup=popup, 
            icon=folium.Icon(color='blue', icon='star')).add_to(map)

# map.save('./Day3/dataZ/map08.html')
# webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map08.html'))
map.save('../Data/dataZ/map08.html')
webbrowser.open('file://'+os.path.realpath('../Data/dataZ/map08.html'))