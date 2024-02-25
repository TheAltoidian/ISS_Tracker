import requests
from datetime import datetime

MY_LAT = 37.547150
MY_LONG = -122.314400

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])



#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
# print(f"iss_lat: {iss_latitude}\niss_lon: {iss_longitude}\ntime_now: {time_now}\nparameters : {parameters}\nsunrise: {sunrise}\nsunset: {sunset}")

# Check if the ISS is overhead, with a 5 degree margin of error
lat_distance = abs(iss_longitude - MY_LONG)
lon_distance = abs(iss_latitude - MY_LAT)
if lat_distance <= 5:
    if lon_distance <= 5:
        # Check if it's dark outside
        if time_now >= sunset or time_now <= sunrise:
            print("ISS is above!")

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



