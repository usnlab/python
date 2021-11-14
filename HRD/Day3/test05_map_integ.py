import folium
import os
import webbrowser
import pandas as pd
from folium.plugins import MarkerCluster

location1 = [37.555403, 126.937188]

# folium.Marker(location=location1, popup='LearningCenter', icon=folium.Icon(icon='coffee',color='red',prefix='fa')).add_to(map)
# folium.CircleMarker(location=location1, popup='Boundary', radius=100, color='#3186cc', fill_color='#3186cc').add_to(map)
# map.save('./Day3/dataZ/map01.html')
# webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map01.html'))

df = pd.read_csv('./Day3/data/Seoul_Store_202109.csv')
data = df[df['상권업종대분류명'].str.contains('음식', na=False)]
#print(data)
map = folium.Map(location1, zoom_start=12)
latlon = data[['위도','경도']]
mc = MarkerCluster().add_to(map)

for lat, lon in zip(latlon.위도, latlon.경도):
    folium.Marker(location=[lat,lon],icon=folium.Icon(color='red')).add_to(mc)

map.save('./Day3/dataZ/map02.html')
webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map02.html'))