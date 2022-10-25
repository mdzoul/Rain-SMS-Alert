"""This code send an SMS to user if rainy weather"""
import requests
from twilio.rest import Client

API_KEY = "e533f7259074449702b57be13b4cdc3e"
PARAMETERS = {
    "lat": 1.3408630000000001,
    "lon": 103.83039182212079,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}
WILL_RAIN = False
ACCOUNT_SID = "AC3759af84b38e8b8c8db11d9d3e01f43a"
AUTH_TOKEN = "65d4359bc6fca2d153f79732249f8b9d"

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
        from_="+15017122661",  # TODO: Change this number once account is unrestricted
        to="+6582289433"
    )
    print(message.status)
