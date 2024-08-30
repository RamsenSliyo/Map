import pandas as pd
import folium as F

longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472

# map starter med madrids koordinater
map = F.Map(location=(40.4,-3.68,), zoom_start=12)

# Tilføj markører fra CSV-filen
for _, row in longboi.iterrows():
    F.Marker((row['latitude'], row['longitude']), popup=row['name']).add_to(map)

# MARKER
F.Marker((40.41420851217709, -3.7038109414543245), popup='THE HOTEL').add_to(map)
F.Marker((56.15625970328441, 10.187543466182403), popup='HELVEDE').add_to(map)
F.Marker((40.420487070674056, -3.708046910981905), popup='Cafe Oskar med K ').add_to(map)

# Linjer
F.PolyLine(locations=[(40.41420851217709, -3.7038109414543245), (40.420487070674056, -3.708046910981905)]).add_to(map)
F.PolyLine(locations=[(40.41420851217709, -3.7038109414543245), (56.15625970328441, 10.187543466182403)]).add_to(map)


map.show_in_browser()
map.save("Map.html")
input("wait for exit")