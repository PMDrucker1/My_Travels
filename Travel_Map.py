import folium
import pandas

data = pandas.read_csv("Peter_Travel_Map_Data.txt")

lon = list(data["LON"])
lat = list(data["LAT"])
location = list(data["LOCATION"])
name = list(data["NAME"])

map = folium.Map(location=[42.5, -74], zoom_start=3, tiles='Stamen Terrain')

fg = folium.FeatureGroup(name="Peter's Map")

for lt, ln, el, nm in zip(lat, lon, location, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Peter's_Travel_Map.html")
