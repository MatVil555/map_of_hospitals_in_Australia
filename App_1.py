import folium as fl
import pandas as pd

b1=pd.read_csv('myhospitals_contact_details.csv', encoding = "ISO-8859-1")

def color_producer():
    return 'red'


mapp=fl.Map( [ -25.2744,133.7751], zoom_start=6)
fgh=fl.FeatureGroup(name='My_map_hostpitals')
fgp=fl.FeatureGroup(name='My_map_pop')            
for i,j,k,phone in zip(b1['Latitude'],b1['Longitude'],b1['Hospital name'],b1['Phone number']):

               fgh.add_child(fl.CircleMarker(location=[i,j], radius=5,
                                            popup=f'Name: {k} \n Phone number: {phone}', draggable=True, fill_color='yellow', color='grey', fill_opacity=0.7))


fgp.add_child(fl.GeoJson(data=(open('world.json','r', encoding = 'utf-8-sig').read()),
             style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005']>10000000 else 'blue'}))




mapp.add_child(fgp)
mapp.add_child(fgh)
mapp.add_child(fl.LayerControl())

mapp.save('Map_1.html')