"""
Stock Trading news alerts.
"""
import os
from datetime import date, timedelta

import requests
from twilio.rest import Client

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
ALPHAVANTAGE_URL = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

NEWSAPI_URL = "https://newsapi.org/v2/everything"
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


def get_previous_days_date(
    days_past_from_date_: int, date_: date = None, date_format: str = "%Y-%m-%d"
) -> str:
    if date_ is None:
        date_ = date.today()
    return (date_ - timedelta(days=days_past_from_date_)).strftime(date_format)


alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHAVANTAGE_API_KEY,
}

try:
    res = requests.get(ALPHAVANTAGE_URL, params=alphavantage_params)
    res.raise_for_status()
except requests.exceptions.HTTPError as http_err:
    print(f"Unable to fetch the response from the url - {http_err}")
else:
    try:
        json_res = res.json()
        yesterday = get_previous_days_date(1)
        yesterday_data = json_res["Time Series (Daily)"][yesterday]
    except KeyError:
        last_refreshed_date = json_res["Meta Data"]["3. Last Refreshed"]
        year_, month_, date_ = last_refreshed_date.split("-")
        today_ = date(int(year_), int(month_), int(date_))
        yesterday = get_previous_days_date(1, today_)
        yesterday_data = json_res["Time Series (Daily)"][yesterday]
        day_before_yesterday = get_previous_days_date(2, today_)
        day_before_yesterday_data = json_res["Time Series (Daily)"][
            day_before_yesterday
        ]
    else:
        day_before_yesterday = get_previous_days_date(2)
        day_before_yesterday_data = json_res["Time Series (Daily)"][
            day_before_yesterday
        ]

yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
)

diff_in_percentage = (difference / float(yesterday_closing_price)) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if diff_in_percentage < 1:
    newsapi_params = {
        "q": COMPANY_NAME,
        "apikey": NEWSAPI_API_KEY,
    }

    newsapi_res = requests.get(NEWSAPI_URL, params=newsapi_params)
    articles = newsapi_res.json().get("articles")[:3]
    news = [
        f"Headline: {article['title']}, \nBrief: {article['description']}"
        for article in articles
    ]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for new in news:
        message = twilio_client.messages.create(
            body=new,
            from_="+12017293244",
            to="+91 81494 84184",
        )
