"""This code send an SMS to user if rainy weather"""
import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("API_KEY")
PARAMETERS = {
    "lat": 1.3408630000000001,
    "lon": 103.83039182212079,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}
WILL_RAIN = False
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM_NUM = os.environ.get("FROM_NUM")
TO_NUM = os.environ.get("TO_NUM")

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=PARAMETERS)
response.raise_for_status()
data = response.json()
hourly_forecast = data["hourly"]

for hour in hourly_forecast[:18]:
    condition_code = hour["weather"][0]["id"]
    if condition_code < 700:
        WILL_RAIN = True

if WILL_RAIN:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella! ☔️",
        from_=FROM_NUM,
        to=TO_NUM
    )
    print(message.status)
