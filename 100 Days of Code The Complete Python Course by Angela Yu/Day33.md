# Day 33: API Endpoints & API Parameters - ISS Overhead Notifier

Welcome to my log for Day 33! Today, I learned how to connect my Python programs to the wider world by working with Application Programming Interfaces (APIs). An API acts as an interface that allows different software applications to communicate with each other. I learned how to use the `requests` library to make API calls, handle different response codes, and work with API parameters to customize the data I receive. The final project was to build a program that tracks the International Space Station (ISS) and notifies me via email when it's overhead and dark outside.


## Table of Contents
- [1. What is an API?](#1-what-is-an-api)
- [2. Making API Requests with Python](#2-making-api-requests-with-python)
- [3. API Parameters](#3-api-parameters)
- [4. Project: ISS Overhead Notifier](#4-project-iss-overhead-notifier)
- [5. Final Project Code](#5-final-project-code)

---

### 1. What is an API?
An API is a set of rules and definitions that allows one computer application to "talk" to another. In the context of this lesson, it's how my Python script can request and receive live data from a server on the internet.

-   **API Endpoint:** This is simply a URL that points to the location of the data I want to access. For example, the endpoint for the current ISS location is `http://api.open-notify.org/iss-now.json`.
-   **API Request:** This is the message my program sends to the API endpoint to ask for data. The simplest type is a `GET` request, which is used to retrieve data.
-   **API Response & JSON:** When the server receives a valid request, it sends back a response, often in JSON format. JSON is perfect for this because it's lightweight and easily converts to a Python dictionary.

---

### 2. Making API Requests with Python
To interact with APIs, I used the `requests` library, which is the standard for making HTTP requests in Python.

-   **Installation:** `requests` is not a built-in library, so it needs to be installed first.
-   **Making a GET Request:** I used `requests.get(url="...")` to send a request to the API endpoint.
-   **Handling Responses:**
    -   The `requests.get()` function returns a `Response` object.
    -   **Response Codes:** The status of the request is indicated by a response code (e.g., `200` means success, `404` means not found). I can check this with `response.status_code`.
    -   **Raising Exceptions:** Instead of checking every possible status code manually, I can use `response.raise_for_status()`. This will automatically raise an `HTTPError` if the request was unsuccessful, stopping the program and showing me what went wrong.
    -   **Getting the Data:** To get the actual data from the response, I call `.json()`, which parses the JSON response into a Python dictionary.

```python
import requests

response = requests.get(url="[http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)")
response.raise_for_status() # Will raise an exception for bad responses (4xx or 5xx)

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
```

---

### 3. API Parameters
Some APIs allow or require you to provide parameters to customize the request. For instance, a weather API needs to know *which* city's weather you want.

-   **What are they?** Parameters are key-value pairs that are sent along with the API request to specify what data you're looking for.
-   **How to use them?** With the `requests` library, I can pass a dictionary of parameters to the `params` argument in the `get()` function. The library handles formatting the URL correctly.

```python
# Example for a weather API that requires latitude and longitude
parameters = {
    "lat": 51.507351,
    "lng": -0.127758,
    "formatted": 0, # An optional parameter to get raw time data
}

response = requests.get("[https://api.sunrise-sunset.org/json](https://api.sunrise-sunset.org/json)", params=parameters)
```

---

### 4. Project: ISS Overhead Notifier
The project of the day was to build a program that alerts me when the ISS is flying over my location, but only if it's dark outside.

-   **My Process:**
    1.  **Get My Location:** I defined my latitude and longitude as constants.
    2.  **Get ISS Position:** I made an API call to the Open Notify API to get the current latitude and longitude of the ISS.
    3.  **Check if ISS is Close:** I wrote a function `is_iss_overhead()` that checks if the ISS's current coordinates are within +/- 5 degrees of my own coordinates.
    4.  **Check if it's Night:** I wrote another function `is_night()` that:
        -   Makes an API call to the Sunrise-Sunset API, passing my coordinates as parameters.
        -   Retrieves the sunrise and sunset times for my location.
        -   Gets the current hour using the `datetime` module.
        -   Returns `True` if the current hour is after sunset or before sunrise.
    5.  **Send Email Notification:** If both `is_iss_overhead()` and `is_night()` return `True`, the program uses `smtplib` to send me an email with the subject "Look Up! 🛰️".
    6.  **Automate the Check:** Finally, I wrapped the main logic in a `while True:` loop and added a `time.sleep(60)` at the end. This makes the program run the checks every 60 seconds automatically.

---

### 5. Final Project Code

```python
# main.py
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "YOUR_EMAIL@gmail.com"
MY_PASSWORD = "YOUR_APP_PASSWORD"
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

def is_iss_overhead():
    response = requests.get(url="[http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("[https://api.sunrise-sunset.org/json](https://api.sunrise-sunset.org/json)", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )
```