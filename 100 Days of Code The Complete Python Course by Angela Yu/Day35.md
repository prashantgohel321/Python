# Day 35: API Keys, Authentication & SMS

Welcome to my log for Day 35! Today was all about leveling up my API skills. I learned how to work with APIs that require authentication, which is crucial for accessing more valuable or sensitive data. This involved understanding API keys and, importantly, how to keep them secure using environment variables. I then put this into practice by building a Rain Alert application that checks the weather and sends me an SMS notification using the Twilio API.


## Table of Contents
- [1. API Authentication with API Keys](#1-api-authentication-with-api-keys)
- [2. Securely Storing API Keys with Environment Variables](#2-securely-storing-api-keys-with-environment-variables)
- [3. Sending SMS with the Twilio API](#3-sending-sms-with-the-twilio-api)
- [4. Project: Rain Alert App](#4-project-rain-alert-app)
- [5. Final Project Code](#5-final-project-code)

---

### 1. API Authentication with API Keys
Many APIs, especially those that provide valuable data (like weather forecasts), require you to authenticate yourself before you can make a request. This is usually done with an API key.

-   **What is an API Key?** An API key is a unique string of characters that the API provider gives you. When you make a request, you include this key to identify yourself. It allows the provider to track your usage and ensure you're not abusing their service.
-   **How it Works:** For the OpenWeatherMap API, I had to pass my API key as a parameter in the request. If the key is valid, I get the data; if not, I get a `401 Unauthorized` error.

```python
# Example of API parameters with an API key
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": "YOUR_API_KEY_HERE", # My unique API key
    "cnt": 4, # Only get the next 4 forecasts (12 hours)
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
```

---

### 2. Securely Storing API Keys with Environment Variables
It is a **very bad idea** to hardcode secret keys, passwords, or tokens directly into your code. If you share your code or upload it to a public place like GitHub, your keys will be exposed. The proper way to handle this is with environment variables.

-   **What are they?** Environment variables are variables that are part of the environment in which your code runs (e.g., your operating system or a server like PythonAnywhere). They are stored separately from the code itself.
-   **How to Use Them in Python:**
    1.  First, `import os`.
    2.  Set the variable in your terminal (or the configuration of your server). For example: `export OWM_API_KEY="your_actual_key"`
    3.  In your Python script, access the variable using `os.environ.get("OWM_API_KEY")`. The `.get()` method is safer because it returns `None` if the variable isn't found, instead of crashing the program.

---

### 3. Sending SMS with the Twilio API
Twilio is a powerful service that allows developers to programmatically send and receive SMS messages, make phone calls, and more.

-   **How it works:**
    1.  **Sign Up:** I created a free trial account on Twilio, which gave me a trial phone number, an Account SID, and an Auth Token.
    2.  **Install the Library:** Twilio has a Python helper library that makes interacting with their API very simple.
    3.  **Send a Message:** Using my Account SID, Auth Token, and trial number, I could create a `client` object and use it to send an SMS message to my verified phone number.

---

### 4. Project: Rain Alert App
The goal of the project was to create a Python script that checks the weather for the next 12 hours and sends an SMS to my phone if rain is forecasted.

-   **My Process:**
    1.  **Fetch Weather Data:** The script makes a request to the OpenWeatherMap "5 Day / 3 Hour Forecast" API, using my location and API key. I set the `cnt` parameter to `4` to get just the next four 3-hour forecasts (a 12-hour window).
    2.  **Check for Rain:** I looped through the four forecast periods. For each period, I checked the weather condition code. According to the documentation, any code less than 700 indicates some form of precipitation (rain, snow, drizzle, etc.). If I found any such code, a flag `will_rain` was set to `True`.
    3.  **Send SMS Notification:** If `will_rain` was true, the script then used the Twilio API to send an SMS to my phone with the message: "It's going to rain today. Remember to bring an ☂️".
    4.  **Automation:** I deployed the final script to PythonAnywhere and set up a scheduled task to run it every morning, ensuring I'd get a rain alert before leaving the house.

---

### 5. Final Project Code

```python
# main.py
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# --- OpenWeatherMap API ---
OWM_Endpoint = "[https://api.openweathermap.org/data/2.5/forecast](https://api.openweathermap.org/data/2.5/forecast)"
api_key = os.environ.get("OWM_API_KEY")

# --- Twilio API ---
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 22.303894,
    "lon": 70.802162,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="YOUR_TWILIO_TRIAL_NUMBER",
        to="YOUR_VERIFIED_PHONE_NUMBER"
    )
    print(message.status)
```