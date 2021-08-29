"""
OpenWeather API

Required environment variables
OpenWeather - api_key
Twilio - account_sid, auth_token
"""

import os

import requests
from twilio.rest import Client

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
LATITUDE = 10.786999
LONGITUDE = 79.137825

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

URL = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily,alerts",
    "appid": OPENWEATHER_API_KEY,
}

res = requests.get(URL, params=params)
res.raise_for_status()
weather_datas = res.json()
hourly_weather_datas = weather_datas.get("hourly")

will_rain = False
for hourly_weather_data in hourly_weather_datas[:12]:
    weather_data = hourly_weather_data.get("weather")[0]
    id = weather_data.get("id")
    if id < 700:
        will_rain = True

if will_rain:
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = twilio_client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella!",
        from_="+12017293244",
        to="+91 81449 81844",
    )

print(message.status)
