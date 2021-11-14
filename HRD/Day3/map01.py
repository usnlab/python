import folium
import os
import webbrowser

"""
# 37.555403, 126.937188 : 18-78 Changcheon-dong, Seodaemun-gu, Seoul
map = folium.Map(location=[37.555403, 126.937188], zoom_start=17)
map.save('./Day3/dataZ/map01.html')
webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map01.html'))
"""

# 37.555403, 126.937188 : 18-78 Changcheon-dong, Seodaemun-gu, Seoul
location1 = [37.555403, 126.937188]
#map = folium.Map(location1, zoom_start=17, tiles='Stamen Terrain')   # Tile 지정 가능 
map = folium.Map(location1, zoom_start=17)

# prefix 없으면 icon 이 안 나옴
folium.Marker(location=location1, popup='LearningCenter', icon=folium.Icon(icon='coffee',color='red',prefix='fa')).add_to(map)
# 기본적으로 map 은 browser 에서 나오므로, html 형태로 저장하고, browser 에서 open 한다. 

folium.CircleMarker(location=location1, popup='Boundary', radius=100, color='#3186cc', fill_color='#3186cc').add_to(map)

map.save('./Day3/dataZ/map01.html')
webbrowser.open('file://'+os.path.realpath('./Day3/dataZ/map01.html'))