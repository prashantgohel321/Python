# Day 37: Advanced API Requests & Habit Tracker

Welcome to my log for Day 37! Today, I delved into more advanced ways of interacting with APIs. I moved beyond just fetching data and learned how to send `POST`, `PUT`, and `DELETE` requests to create, update, and delete data on a server. I also learned about a more secure method of API authentication using request headers. I applied these new skills to build a personal Habit Tracker that uses the Pixela API to visualize my progress.


## Table of Contents
- [1. Understanding `POST`, `PUT`, and `DELETE` Requests](#1-understanding-post-put-and-delete-requests)
- [2. Authentication via Request Headers](#2-authentication-via-request-headers)
- [3. Project: Habit Tracker with Pixela API](#3-project-habit-tracker-with-pixela-api)
- [4. Formatting Dates with `strftime`](#4-formatting-dates-with-strftime)
- [5. Final Project Code](#5-final-project-code)

---

### 1. Understanding `POST`, `PUT`, and `DELETE` Requests
So far, I've primarily used `GET` requests to retrieve data from APIs. Today, I learned about other crucial HTTP methods:

-   **`POST`**: Used to send data to a server to create a new resource. For example, creating a new user account or posting a new pixel to my habit graph.
-   **`PUT`**: Used to update an existing resource on the server. I used this to change the quantity for a specific day on my habit graph.
-   **`DELETE`**: Used to remove a resource from the server. I used this to delete a pixel from a specific day.

The `requests` library in Python makes these calls just as simple as `GET` requests: `requests.post()`, `requests.put()`, and `requests.delete()`.

---

### 2. Authentication via Request Headers
Previously, I passed my API keys as URL parameters. A more secure and common method is to send them in the request header.

-   **Why use Headers?** Sending sensitive information like an API key in the header prevents it from being logged in server histories or exposed in the URL itself, making it much more secure.
-   **How to Implement:** The `requests` library allows you to pass a dictionary of headers using the `headers` parameter. The API documentation (like Pixela's) specifies the exact header key needed (e.g., `X-USER-TOKEN`).

```python
headers = {
    "X-USER-TOKEN": "YOUR_SECRET_TOKEN"
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
```

---

### 3. Project: Habit Tracker with Pixela API
The day's project was to build a script that interacts with the Pixela API, a unique service for creating "pixel"-based habit graphs.

-   **My Process:**
    1.  **Create a User (`POST`):** The first step was to make a `POST` request to the Pixela user endpoint to create a new user account, which required a self-generated token and a username.
    2.  **Create a Graph (`POST`):** Next, I made another `POST` request to the graph endpoint to define a new graph. This required an ID, a name, unit of measurement (e.g., "Km"), data type (e.g., "float"), and color. This request needed my user token in the header for authentication.
    3.  **Post a Pixel (`POST`):** To log a habit for a specific day, I sent a `POST` request to the graph's pixel endpoint. The body of the request contained the date and the quantity (e.g., how many kilometers I cycled).
    4.  **Update/Delete Pixels (`PUT`/`DELETE`):** I also practiced updating a pixel with a new value using a `PUT` request and removing it entirely with a `DELETE` request.

---

### 4. Formatting Dates with `strftime`
The Pixela API required dates to be in a specific format (`yyyyMMdd`). Python's `datetime` module has a powerful method, `strftime` (string format time), that makes this easy. It uses special codes (like `%Y` for the full year, `%m` for the month, and `%d` for the day) to format a datetime object into any string representation I need.

```python
from datetime import datetime

today = datetime.now()
formatted_date = today.strftime("%Y%m%d") # e.g., "20250912"
```

---

### 5. Final Project Code

```python
# main.py
import requests
from datetime import datetime

# --- Constants ---
USERNAME = "YOUR_UNIQUE_USERNAME"
TOKEN = "YOUR_SELF_GENERATED_TOKEN"
GRAPH_ID = "graph1"

# --- Pixela Endpoints ---
PIXELA_ENDPOINT = "[https://pixe.la/v1/users](https://pixe.la/v1/users)"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

# --- User Creation (Run Once) ---
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# --- Graph Creation (Run Once) ---
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# --- Posting a Pixel ---
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

# --- Updating a Pixel (PUT) ---
# update_endpoint = f"{PIXEL_POST_ENDPOINT}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "4.5"
# }
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# --- Deleting a Pixel (DELETE) ---
# delete_endpoint = f"{PIXEL_POST_ENDPOINT}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
```