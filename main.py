import requests
from twilio.rest import Client
import os


API_KEY = os.environ("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

LAT = "40.712776"
LONG = "-74.005974"

parameters = {
    "lat" : LAT,
    "lon" : LONG,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
forcast_data = response.json()["list"]

will_rain = False
for hour in forcast_data:
    condition_code = hour["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        body="sms_event_notifications",
        to="+14794699464",
        from_="+17372324091",
    )
    print(message.body)

