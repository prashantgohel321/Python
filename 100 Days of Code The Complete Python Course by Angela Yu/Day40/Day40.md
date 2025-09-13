# Day 40: Capstone Project - Flight Deal Finder (Part 2)

Welcome to my log for Day 40! This is the exciting conclusion to the Flight Deal Finder capstone project. Today, I leveled up the personal tool from yesterday into a full-fledged service capable of managing and notifying multiple users. The "Flight Club" is now open for business! It can sign up new members, find more complex flight routes, and automatically email the best deals to everyone on the list.


## Table of Contents
- [1. From Personal Tool to Multi-User Service](#1-from-personal-tool-to-multi-user-service)
- [2. Step 1: Creating a User Sign-Up System](#2-step-1-creating-a-user-sign-up-system)
- [3. Step 2: Finding Flights with Stopovers](#3-step-2-finding-flights-with-stopovers)
- [4. Step 3: Managing and Retrieving User Data](#4-step-3-managing-and-retrieving-user-data)
- [5. Step 4: Emailing Deals to All Club Members](#5-step-4-emailing-deals-to-all-club-members)
- [6. Final Project Code (Part 2)](#6-final-project-code-part-2)

---

### 1. From Personal Tool to Multi-User Service
The main goal today was to scale the application. Instead of sending an SMS only to myself, the program needed to handle a list of users, find deals relevant to them, and send out mass email notifications. This required adding a user management component and upgrading the notification system.

---

### 2. Step 1: Creating a User Sign-Up System
To get users into the system without building a full web application, I used a clever and efficient workaround:

-   **Google Forms:** I created a simple Google Form to act as the sign-up page. It collects the user's First Name, Last Name, and Email.
-   **Linking to Google Sheets:** I linked the form to my existing "Flight Deals" Google Sheet. This automatically created a new sheet tab named "users" and populates it with every new sign-up. This is a fantastic "low-code" approach to user registration.

---

### 3. Step 2: Finding Flights with Stopovers
The original flight search was limited to direct flights, which meant missing out on many potential deals, especially for long-haul destinations. I upgraded the search logic to be more comprehensive:

-   **Two-Phase Search:** The `FlightSearch` class now performs a search for direct flights first.
-   **Fallback Search:** If no direct flights are found for a destination, it automatically triggers a second search for flights with one stopover.
-   **Updated Data Model:** I updated the `FlightData` class to include a `stops` attribute, allowing me to track and report whether a flight is direct or has stopovers.

---

### 4. Step 3: Managing and Retrieving User Data
With user data now flowing into the Google Sheet, I needed a way to access it.

-   **Updated DataManager:** I modified the `DataManager` class to handle the new "users" sheet.
-   **`get_customer_emails()` Method:** I added a new method that makes a `GET` request to the Sheety endpoint for the "users" sheet. It then parses the JSON response and returns a simple list of all registered customer email addresses.

---

### 5. Step 4: Emailing Deals to All Club Members
This was the final piece of the puzzle, turning the notification system into a broadcast tool.

-   **From SMS to Email:** I refactored the `NotificationManager` to send emails instead of SMS messages.
-   **`send_emails()` Method:** This new method uses Python's built-in `smtplib` library. When the main script finds a cheap flight, it now calls this method.
-   **Mass Emailing:** The method takes the flight deal message and the list of customer emails (from `DataManager`) as input. It then iterates through the list, sending a formatted email alert to every single user in the club. I also had to handle character encoding (`.encode('utf-8')`) to ensure symbols like `£` were transmitted correctly.

---

### 6. Final Project Code (Part 2)
Here is the complete, final code for all modules of the Flight Club project.

```python
# data_manager.py
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint)
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
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
            
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
```

```python
# flight_data.py
class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops=0):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
    if data is None or not data['data']:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            # Update with cheaper flight details
            lowest_price = price
            # ... (rest of the parsing logic) ...
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
            
    return cheapest_flight
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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        if response.status_code != 200:
            return None
        return response.json()
```

```python
# notification_manager.py
import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        # ... SMS sending logic ...
        pass

    def send_emails(self, email_list, email_body):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(self.email, self.email_password)
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
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

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

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

    if cheapest_flight.price == "N/A":
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, with {cheapest_flight.stops} stop(s), from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
        
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)
```