
#pip install phonenumbers
import phonenumbers

phn_number="+8801751594755"

from phonenumbers import geocoder
samNumber=phonenumbers.parse(phn_number)

yourlocation=geocoder.description_for_number(samNumber,"en")
print(yourlocation)

#number provider
from phonenumbers import carrier

number_provider=phonenumbers.parse(phn_number)
print(carrier.name_for_number(number_provider,"en"))


#pip3 install opencage
key='88dff1a47bf84759afd391791893ed6c'
from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(key)

quary=str(yourlocation)
result=geocoder.geocode(quary)
print(result)

lat= result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']

print(lat,lng)

#pip install folium
import folium

map=folium.Map(location=[lat,lng],Zoom_start=9)

folium.Marker([lat,lng],popup=yourlocation).add_to(map)
map.save("Location.html")

