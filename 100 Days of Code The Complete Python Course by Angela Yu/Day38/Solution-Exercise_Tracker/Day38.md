# Day 38: Workout Tracking with Natural Language Processing & Google Sheets

Welcome to my log for Day 38! This was a "build-it-yourself" challenge project where I created a workout tracking application. The app's coolest feature is its use of natural language processing: I can type a sentence like "I ran 3 miles and swam for 20 minutes," and the program automatically figures out the exercises, durations, and calories burned. It then logs all of this data neatly into a personal Google Sheet. This project was a fantastic exercise in combining multiple APIs and managing authentication securely.


## Table of Contents
- [1. Project Overview & My Step-by-Step Plan](#1-project-overview--my-step-by-step-plan)
- [2. Step 1: Setting up API Credentials](#2-step-1-setting-up-api-credentials)
- [3. Step 2: Processing Natural Language with the Nutritionix API](#3-step-2-processing-natural-language-with-the-nutritionix-api)
- [4. Step 3 & 4: Saving Data to Google Sheets with the Sheety API](#4-step-3--4-saving-data-to-google-sheets-with-the-sheety-api)
- [5. Step 5 & 6: Securing the App with Authentication & Environment Variables](#5-step-5--6-securing-the-app-with-authentication--environment-variables)
- [6. Final Project Code](#6-final-project-code)

---

### 1. Project Overview & My Step-by-Step Plan
The goal was to create a Python script that takes a plain English sentence describing a workout, sends it to an API to get structured exercise data (like duration and calories), and then saves that data as a new row in a Google Sheet.

**My Step-by-Step Plan:**
1.  **Set up Credentials:** Get API keys from Nutritionix (for exercise data) and set up a Google Sheet to act as my database.
2.  **Natural Language Processing:** Use the Nutritionix API to make a `POST` request. The body of the request would be my plain text query (e.g., "cycled for 30 minutes").
3.  **Connect to Google Sheets:** Use the Sheety API to turn my Google Sheet into a simple API that I can send data to.
4.  **Save the Data:** Loop through the structured exercise data returned from Nutritionix and make a `POST` request to my Sheety endpoint for each exercise, creating a new row in the spreadsheet.
5.  **Add Authentication:** Secure the Sheety endpoint so that only my script can add data to it.
6.  **Secure API Keys:** Remove all hardcoded keys, tokens, and personal data from the script and store them as environment variables.

---

### 2. Step 1: Setting up API Credentials
-   **Google Sheet:** I created a copy of a template Google Sheet with columns for `Date`, `Time`, `Exercise`, `Duration`, and `Calories`.
-   **Nutritionix API:** I signed up for a free developer account on the Nutritionix website to get my `APP_ID` and `API_KEY`. These are required for authenticating all requests.

---

### 3. Step 2: Processing Natural Language with the Nutritionix API
This API does the heavy lifting of understanding human language.

-   **API Endpoint:** I sent a `POST` request to the `/v2/natural/exercise` endpoint.
-   **Authentication:** The request required my `x-app-id` and `x-app-key` to be sent in the request headers.
-   **Request Body:** The JSON body of the request included my `query` (the sentence I typed) as well as personal stats like gender, weight, height, and age, which are used to calculate calories more accurately.
-   **Response:** The API returns a JSON object containing a list of `exercises` it identified, complete with structured data like `name`, `duration_min`, and `nf_calories`.

---

### 4. Step 3 & 4: Saving Data to Google Sheets with the Sheety API
Sheety is a brilliant service that turns any Google Sheet into a REST API almost instantly.

-   **Setup:** I logged into Sheety, created a new project, and linked it to my "My Workouts" Google Sheet. Sheety provided me with a unique API endpoint for my sheet.
-   **Making the `POST` Request:** After getting the exercise data from Nutritionix, I looped through each exercise. For each one, I created a dictionary formatted exactly as Sheety requires. Then, I made a `POST` request to my Sheety endpoint with this dictionary as the JSON body. This action automatically added a new row to my Google Sheet.

---

### 5. Step 5 & 6: Securing the App with Authentication & Environment Variables
Leaving an open API endpoint to my personal spreadsheet is a bad idea.

-   **Bearer Token Authentication:** I configured my Sheety project to require "Bearer Token" authentication. This meant I had to generate a secret token.
-   **Authorization Header:** To make authenticated requests, I had to include an `Authorization` header in my `POST` request to Sheety. The value was the word "Bearer" followed by my secret token.
-   **Environment Variables:** Finally, I moved all my sensitive data—Nutritionix ID and Key, Sheety endpoint URL, and the Sheety Bearer Token—out of my code and into environment variables. This is a critical security practice to avoid exposing secrets.

---

### 6. Final Project Code

```python
# main.py
import requests
from datetime import datetime
import os

# --- Constants & Environment Variables ---
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 30

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")

# --- Nutritionix API Call ---
exercise_endpoint = "[https://trackapi.nutritionix.com/v2/natural/exercise](https://trackapi.nutritionix.com/v2/natural/exercise)"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# --- Sheety API Call ---
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT, 
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
```