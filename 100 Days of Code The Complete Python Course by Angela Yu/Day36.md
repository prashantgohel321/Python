# Day 36: Stock Trading News Alert Project

Welcome to my log for Day 36! Today's project was my most complex API integration yet: building a stock news monitoring service. The goal was to create a Python script that tracks a specific stock (like Tesla), detects significant price changes (e.g., more than 5% in a day), and then automatically fetches and sends the top 3 related news articles to my phone via SMS. It was a fantastic exercise in problem decomposition and API orchestration.


## Table of Contents
- [1. Project Overview & Problem Decomposition](#1-project-overview--problem-decomposition)
- [2. Fetching Stock Data with Alpha Vantage](#2-fetching-stock-data-with-alpha-vantage)
- [3. Calculating the Percentage Change](#3-calculating-the-percentage-change)
- [4. Fetching Relevant News with the News API](#4-fetching-relevant-news-with-the-news-api)
- [5. Sending Formatted SMS Alerts with Twilio](#5-sending-formatted-sms-alerts-with-twilio)
- [6. Final Project Code](#6-final-project-code)

---

### 1. Project Overview & Problem Decomposition
This project was a "build-it-yourself" challenge. The first and most crucial step was breaking down the large, complex goal into a series of smaller, solvable problems.

**My Step-by-Step Plan:**
1.  **Get Stock Prices:** Fetch yesterday's and the day-before-yesterday's closing stock prices for a specific company (e.g., TESLA).
2.  **Calculate Difference:** Find the percentage difference between these two prices.
3.  **Set a Trigger:** If the percentage difference is above a certain threshold (I used 5%), proceed to the next step.
4.  **Get News:** If triggered, fetch the top 3 most recent news articles related to the company.
5.  **Format and Send:** Format the news headlines and descriptions into readable SMS messages and send them using Twilio.

---

### 2. Fetching Stock Data with Alpha Vantage
To get the stock data, I used the Alpha Vantage API, which provides free access to historical and real-time stock market data.

-   **Authentication:** I signed up for a free API key, which was required for all requests.
-   **API Call:** I made a `GET` request to the `TIME_SERIES_DAILY` endpoint.
-   **Parameters:** My request included three parameters:
    -   `function`: Set to `TIME_SERIES_DAILY`.
    -   `symbol`: The stock ticker I was interested in (e.g., `TSLA`).
    -   `apikey`: My unique API key.
-   **Data Parsing:** The JSON response was a nested dictionary. I used a list comprehension to convert the time-series data into a list, making it easy to access yesterday's data at `[0]` and the day-before's data at `[1]`.

---

### 3. Calculating the Percentage Change
Once I had the closing prices for both days, the calculation was straightforward.

-   **Find the Difference:** I subtracted the two closing prices and used the `abs()` function to get the positive difference.
-   **Calculate Percentage:** `(difference / yesterday_closing_price) * 100`
-   **Conditional Trigger:** An `if` statement checks if this percentage is greater than my threshold (e.g., `if diff_percent > 5:`). The rest of the code only runs if this condition is met.

---

### 4. Fetching Relevant News with the News API
When the price change was significant, the script needed to find out why by fetching the news.

-   **API Call:** I used the News API's `everything` endpoint.
-   **Parameters:** The key parameters were:
    -   `qInTitle`: I searched for the company name in the article title to ensure relevance.
    -   `apiKey`: My unique News API key.
-   **Slicing the Results:** The API can return many articles. I used Python's list slicing (`articles[:3]`) to grab only the first three articles from the list returned by the API.

---

### 5. Sending Formatted SMS Alerts with Twilio
The final step was to format the collected information and send it to my phone.

-   **Message Formatting:** I created a list of formatted strings. Each string included an up/down emoji (🔺 or 🔻) based on whether the price difference was positive or negative, the stock symbol, the percentage change, and the headline and brief of one of the top three articles.
-   **Sending the SMS:** I looped through my list of three formatted article strings and sent each one as a separate SMS using the Twilio client.

---

### 6. Final Project Code

```python
# main.py
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "[https://www.alphavantage.co/query](https://www.alphavantage.co/query)"
NEWS_ENDPOINT = "[https://newsapi.org/v2/everything](https://newsapi.org/v2/everything)"

# --- API Keys ---
# NOTE: In a real application, these should be environment variables!
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

# --- Stock Price Fetching ---
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((abs(difference) / yesterday_closing_price) * 100)

# --- News Fetching & SMS Sending ---
if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="YOUR_TWILIO_PHONE_NUMBER",
            to="YOUR_PHONE_NUMBER"
        )
        print(message.status)

```