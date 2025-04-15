import phonenumbers
from phonenumbers import geocoder
import folium
from opencage.geocoder import OpenCageGeocode
import time

key = "bb31d74e94384fc3a872452dae87aee2"

# Prompting user for input only once
number = input("Enter Phone Number with Country Code:")

# Parse the number
check_number = phonenumbers.parse(number)

# Get location description
number_location = geocoder.description_for_number(check_number, "en")
print("Location:", number_location)

# Importing carrier class
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
# To know about service provider
print(carrier.name_for_number(service_provider, "en"))

# Using map - OpenCage
geocoder = OpenCageGeocode(key)

# Getting the initial location
query = str(number_location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Latitude:", lat, "Longitude:", lng)

# Creating the map
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)

# Save the initial location to HTML file
map_location.save("mylocation.html")

# Simulating live tracking by refreshing the coordinates (for example, changing location every 5 seconds)
# In a real-life scenario, you would receive updated GPS coordinates.
for _ in range(5):  # Simulate 5 updates for demonstration
    # Simulating new coordinates (add random movement for example purposes)
    lat += 0.0001  # Simulating movement
    lng += 0.0001  # Simulating movement

    # Update the map with new location
    map_location = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup="Tracking Location").add_to(map_location)

    # Save updated map to HTML
    map_location.save("mylocation_updated.html")

    # Wait for 5 seconds before simulating the next update
    time.sleep(5)
