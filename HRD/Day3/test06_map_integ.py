import folium
import os
import webbrowser
import pandas as pd
from folium.plugins import MarkerCluster
import json

location1 = [37.555403, 126.937188]

df = pd.read_csv('./Day3/data/Seoul_Store_202109.csv')
data = df[df['상권업종대분류명'].str.contains('음식', na=False)]

map = folium.Map(location1, zoom_start=12)
latlon = data[['위도','경도']]
mc = MarkerCluster().add_to(map)

for lat, lon in zip(latlon.위도, latlon.경도):
    folium.Marker(location=[lat,lon],icon=folium.Icon(color='red')).add_to(mc)

# Close() 불필요한 syntax (with open)
with open('./Day3/data/seoul_municipalities_geo.json', mode='r', encoding='utf-8') as jsfile :
    bit = json.loads(jsfile.read())

folium.GeoJson(bit, name='Seoul Store & Municipality').add_to(map)

map.save('./Day3/dataZ/map03.html')
webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map03.html'))