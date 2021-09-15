"""
Workout Tracker app
"""
import os
from datetime import datetime

import requests

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

NUTRITIONIX_URL = "https://trackapi.nutritionix.com"
SHEETY_URL = "https://api.sheety.co/8420dc20a8579ba45f5f016acac20771/workouts/workouts"

NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}


def get_date_and_time() -> tuple:
    date_time = datetime.now()
    date_ = date_time.strftime("%d/%m/%Y")
    time_ = date_time.strftime("%X")
    return date_, time_


input_ = input("Tell me which exercises you did?: ")
params = {
    "query": input_,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 190,
    "age": 24,
}

nutritionix_res = requests.post(
    f"{NUTRITIONIX_URL}/v2/natural/exercise", json=params, headers=NUTRITIONIX_HEADERS
).json()
for exercise in nutritionix_res.get("exercises"):
    date_, time_ = get_date_and_time()
    sheety_payload = {
        "workout": {
            "date": date_,
            "time": time_,
            "exercise": exercise.get("user_input").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories"),
        }
    }

    sheety_res = requests.post(
        SHEETY_URL, json=sheety_payload, headers={"Content-Type": "application/json"}
    )
    print(sheety_res.json())
