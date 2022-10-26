import phonenumbers
from phonenumbers import geocoder
import opencage
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import folium
number=int(input("Enter the number: "))
number="+91"+str(number)
print(number)
ch_nmber = phonenumbers.parse(number)
location=geocoder.description_for_number(ch_nmber, "en")
print(location)
service_nmber = phonenumbers.parse(number)
print(carrier.name_for_number(service_nmber, "en"))


key="Paste the API key of your opencage account"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("myLocation.html")