# Day 39: Capstone Project - Flight Deal Finder (Part 1)

Welcome to my log for Day 39! This is the first part of a two-day capstone project to build a comprehensive Flight Deal Finder. The goal is to create a program that automatically checks for cheap flights to my dream destinations and notifies me via SMS when it finds a great deal. This project ties together everything I've learned about APIs, data management, and Object-Oriented Programming.


## Table of Contents
- [1. Project Vision & Architecture](#1-project-vision--architecture)
- [2. Step 1: Managing Destinations with a Google Sheet & Sheety API](#2-step-1-managing-destinations-with-a-google-sheet--sheety-api)
- [3. Step 2: Authenticating with Amadeus API (Bearer Token)](#3-step-2-authenticating-with-amadeus-api-bearer-token)
- [4. Step 3: Finding Airport IATA Codes](#4-step-3-finding-airport-iata-codes)
- [5. Step 4: Searching for the Cheapest Flights](#5-step-4-searching-for-the-cheapest-flights)
- [6. Step 5: Sending SMS Notifications with Twilio](#6-step-5-sending-sms-notifications-with-twilio)
- [7. Final Project Code (Part 1)](#7-final-project-code-part-1)

---

### 1. Project Vision & Architecture
The application works in a logical sequence:
1.  **Read Destinations:** Pull a list of desired travel destinations and my target prices from a Google Sheet.
2.  **Find IATA Codes:** For each city, find its unique IATA airport code, which is necessary for flight searches.
3.  **Search Flights:** For each destination, search for the cheapest flight from my home city within the next six months.
4.  **Compare Prices:** Check if the found flight price is lower than my target price in the Google Sheet.
5.  **Send Alert:** If a deal is found, send a formatted SMS message to my phone with all the flight details.

To keep the code clean and organized, I structured the project into separate classes, each with a single responsibility:
-   `DataManager`: Handles all communication with the Google Sheet via the Sheety API.
-   `FlightSearch`: Manages all flight-related API calls to the Amadeus API.
-   `FlightData`: A simple data class to structure the flight information.
-   `NotificationManager`: Responsible for sending SMS alerts via the Twilio API.

---

### 2. Step 1: Managing Destinations with a Google Sheet & Sheety API
I started by creating a Google Sheet with columns for `City`, `IATA Code`, and `Lowest Price`. Using the Sheety API, I turned this sheet into a simple REST API. The `DataManager` class handles `GET` requests to read the destination data and `PUT` requests to update the sheet with the IATA codes I find later.

---

### 3. Step 2: Authenticating with Amadeus API (Bearer Token)
The Amadeus Flight Search API is a professional-grade service and requires a more secure authentication method than I've used before.

-   **OAuth2 Authentication:** Instead of just sending an API key, I had to make a separate `POST` request to an authentication endpoint with my API Key and API Secret.
-   **Bearer Token:** The server responded with a temporary **Bearer Token**. This token must be included in the `Authorization` header for all subsequent flight search requests. I implemented a method in my `FlightSearch` class to automatically request a new token every time the program runs.

---

### 4. Step 3: Finding Airport IATA Codes
To search for flights, I can't use city names; I need their official IATA codes (e.g., "Paris" -> "PAR").

The `FlightSearch` class has a method that takes a city name, makes a `GET` request to the Amadeus "City Search" endpoint, and returns the corresponding IATA code. My main script then loops through my destinations from the Google Sheet, gets the IATA code for each, and uses the `DataManager` to write these codes back to the sheet.

---

### 5. Step 4: Searching for the Cheapest Flights
This is the core logic of the application.

-   **Search Parameters:** For each destination, the `FlightSearch` class makes a `GET` request to the "Flight Offers Search" endpoint. The parameters specify my origin city (`LON`), the destination IATA code, a date range (from tomorrow to six months from now), and that I only want non-stop flights.
-   **Parsing the JSON:** The API returns a large JSON file with many flight options. I created a helper function, `find_cheapest_flight`, to parse this data, find the flight with the lowest price, and structure the relevant details (price, dates, airports) into a `FlightData` object.

---

### 6. Step 5: Sending SMS Notifications with Twilio
The final step is to alert me when a deal is found.

-   **Comparison:** The main script compares the price of the cheapest flight found by `FlightSearch` against the `lowestPrice` from my Google Sheet for that destination.
-   **Triggering Notification:** If `cheapest_flight.price < destination["lowestPrice"]`, it calls the `NotificationManager`.
-   **Sending SMS:** The `NotificationManager` class formats a message with all the flight details and uses the Twilio API to send it as an SMS to my phone.

---

### 7. Final Project Code (Part 1)
Here is the code for the main modules created today.

```python
# data_manager.py
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            print(response.text)
```

```python
# flight_search.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "[https://test.api.amadeus.com/v1/reference-data/locations/cities](https://test.api.amadeus.com/v1/reference-data/locations/cities)"
FLIGHT_ENDPOINT = "[https://test.api.amadeus.com/v2/shopping/flight-offers](https://test.api.amadeus.com/v2/shopping/flight-offers)"
TOKEN_ENDPOINT = "[https://test.api.amadeus.com/v1/security/oauth2/token](https://test.api.amadeus.com/v1/security/oauth2/token)"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        try:
            code = response.json()["data"][0]['iataCode']
        except (IndexError, KeyError):
            return "N/A"
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "1",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        
        if response.status_code != 200:
            return None

        return response.json()
```

```python
# flight_data.py
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data):
    if data is None or not data.get('data'):
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    # ... parsing logic ...
    
    # For brevity, returning a structured object
    return FlightData(
        price=lowest_price,
        origin_airport=first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
        destination_airport=first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
        out_date=first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
        return_date=first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    )

```

```python
# notification_manager.py
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        print(message.sid)
```

```python
# main.py
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
        )

```