import json
import folium
import os
import webbrowser
from folium import plugins
from folium.map import Icon
import pandas as pd
from folium.plugins import MarkerCluster

location1 = [37.555403, 126.937188]

# with open('./Day3/data/skorea_municipalities_geo_simple.json', mode='r', encoding='utf-8') as jsfile :
#     bit = json.loads(jsfile.read())

geo_str = json.load(open('./Day3/data/skorea_municipalities_geo_simple.json', encoding='utf-8'))
crime_anal = pd.read_csv('./Day3/data/crime_anal_norm.csv', index_col=0)
police = pd.read_csv('./Day3/data/police.csv', index_col=0)


map = folium.Map(location1, zoom_start=14)

for i in range(len(police)):
    location2 = (float(police.iloc[i,2]),float(police.iloc[i,3]))
    folium.Marker(location2, 
                    folium.Popup(html='{0}'.format(police.iloc[i,0]), max_width=400),
                    icon=folium.Icon(icon='building', color='red', prefix='fa')
                ).add_to(map)

# 군집화 
folium.Choropleth(geo_data=geo_str, 
                    data = crime_anal['강도'],
                    columns=[crime_anal.index, crime_anal['강도']],
                    key_on='feature.id',
                    fill_color='Purples',
                    line_color='black',
                    line_weight=1,
                    line_opacity=0.7).add_to(map)

map.save('./Day3/dataZ/map04.html')
webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map04.html'))