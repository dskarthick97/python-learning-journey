""" ISS Overhead Notifier """

from time import sleep
from datetime import datetime

import requests
import smtplib

MY_LATITUDE  = 10.786999
MY_LONGITUDE = 79.137825

SENDER   = "dhilipsabari1997@gmail.com"
PASSWORD = "blahblahblah"

# ISS Now API response
def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"]) 
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if (MY_LATITUDE - 5) <= iss_lat <= (MY_LATITUDE + 5) and \
        (MY_LONGITUDE - 5) <= iss_lng <= (MY_LONGITUDE + 5):
        return True

    return False


# Sunrise and Sunset API response
def is_night():
    LOCATION = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    sun_response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=LOCATION
    )
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = sun_data["results"]["sunrise"]
    sunset  = sun_data["results"]["sunset"]

    sunrise_hr = int(sunrise.split("T")[-1].split(":")[0])
    sunset_hr  = int(sunset.split("T")[-1].split(":")[0])

    now = datetime.now()
    hr  = now.hour

    if hr >= sunset_hr or hr <= sunrise_hr:
        return True

    return False

while True:
    sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER, to_addrs=SENDER, msg="Subject:Look Up for ISS\n\n "
                "The ISS is above you...!"
            )
