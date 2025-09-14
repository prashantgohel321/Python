# Day 47: Amazon Price Tracker

Welcome to my log for Day 47! Today's project was incredibly practical: an **Amazon Price Tracker**. Online prices fluctuate constantly, and manually checking for a price drop is tedious. This project automates that process. The goal was to build a Python bot that scrapes the current price of a product on Amazon and, if the price drops below a target I've set, sends me an email notification with a direct link to buy it.

## Table of Contents
- [1. Project Goal: Never Miss a Deal](#1-project-goal-never-miss-a-deal)
- [2. Step 1: Scraping the Product Price with BeautifulSoup](#2-step-1-scraping-the-product-price-with-beautifulsoup)
- [3. Step 2: Adding Headers to Look Human](#3-step-2-adding-headers-to-look-human)
- [4. Step 3: Sending an Email Alert with SMTPLib](#4-step-3-sending-an-email-alert-with-smtplib)
- [5. Step 4: Securing Credentials with `.env`](#5-step-4-securing-credentials-with-env)
- [6. Day 47 Project: Amazon Price Tracker Code](#6-day-47-project-amazon-price-tracker-code)

---

### 1. Project Goal: Never Miss a Deal
The idea is simple but powerful:
1.  Choose a product on Amazon to track.
2.  Set a target price—the price at which I'm willing to buy.
3.  Have a Python script run automatically (e.g., once a day) to check the current price.
4.  If the current price is less than or equal to my target price, the script sends me an alert email.

This is a perfect application of web scraping and automation, saving both time and money.

---

### 2. Step 1: Scraping the Product Price with BeautifulSoup
The first challenge was to extract the price from a live Amazon product page.
-   **Fetching HTML:** I used the `requests` library to get the HTML content of the product URL.
-   **Parsing HTML:** `BeautifulSoup` was used to parse the raw HTML. By inspecting the Amazon page, I found that the price was contained in a `<span>` with a specific class, such as `a-offscreen`.
-   **Data Cleaning:** The text extracted from the HTML (e.g., "$99.99") isn't a number. I had to clean it by splitting the string to remove the dollar sign `$` and then converting the remaining part into a floating-point number (`float`) so I could perform numerical comparisons.

---

### 3. Step 2: Adding Headers to Look Human
Many large websites, including Amazon, have measures to block scrapers and bots. A simple `requests.get(url)` call can be easily identified as a script.
-   **What are Headers?** When a browser requests a webpage, it sends along extra information called "headers," which include details like the browser type (`User-Agent`) and preferred language (`Accept-Language`).
-   **Mimicking a Browser:** By adding these headers to my request, I make my script look more like a legitimate user visiting the site from a real browser. This significantly reduces the chance of being blocked or served a CAPTCHA page instead of the actual product page. I found my own browser's headers at a site like `http://myhttpheader.com/` and added them to my `requests.get()` call.

---

### 4. Step 3: Sending an Email Alert with SMTPLib
Once the script confirms the price is below the target, it needs to send an alert.
-   **Python's `smtplib`:** This built-in library allows Python to connect to an email server (like Gmail's, Hotmail's, etc.) and send emails.
-   **Conditional Logic:** The email sending code is placed inside an `if` statement: `if current_price < target_price:`.
-   **Composing the Email:** The email body was formatted to be as helpful as possible, including the product title, the new low price, and a direct link to the product page for a quick purchase.
-   **Security (App Passwords):** For services like Gmail, I had to enable 2-Step Verification and generate an "App Password" to allow my script to log in to my account securely without exposing my main password.

---

### 5. Step 4: Securing Credentials with `.env`
Hardcoding my email, password, and SMTP address directly into the Python script is a major security risk, especially if I share the code or upload it to GitHub.
-   **The `dotenv` Library:** I used the `python-dotenv` library to manage my sensitive information.
-   **Creating a `.env` file:** I created a separate file named `.env` (which is typically ignored by version control systems like Git) and stored my credentials as key-value pairs (e.g., `EMAIL_PASSWORD="mypassword"`).
-   **Loading Variables:** In my `main.py`, I used `load_dotenv()` to load these variables into the environment, and then accessed them securely using `os.environ.get("EMAIL_PASSWORD")`. This keeps my credentials out of the source code.

---

### 6. Day 47 Project: Amazon Price Tracker Code
Here is the final, combined code for the project, along with the structure for the `.env` file.

**.env File:**
```
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="your_email@email.com"
EMAIL_PASSWORD="your_app_password_from_google"
```

**main.py:**
```python
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- The product you want to track ---
PRODUCT_URL = "[https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6](https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6)"

# --- Your target price ---
BUY_PRICE = 100.00

# --- Add your browser headers ---
# Find yours here: [http://myhttpheader.com/](http://myhttpheader.com/)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# --- Scrape the Product Page ---
response = requests.get(PRODUCT_URL, headers=header)
soup = BeautifulSoup(response.content, "lxml")

# --- Get the Price ---
try:
    price_span = soup.find(class_="a-offscreen")
    price_str = price_span.get_text()
    price_without_currency = price_str.split("$")[1]
    price_as_float = float(price_without_currency)
except (AttributeError, IndexError) as e:
    print(f"Couldn't find the price. The page structure may have changed. Error: {e}")
    # print(soup.prettify()) # Uncomment to debug the HTML received
    exit()

# --- Get the Product Title ---
title = soup.find(id="productTitle").get_text().strip()

# --- Send Email Alert if Price is Low ---
if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price_as_float}!"

    # Get credentials from environment variables
    my_email = os.environ.get("EMAIL_ADDRESS")
    password = os.environ.get("EMAIL_PASSWORD")
    smtp_address = os.environ.get("SMTP_ADDRESS")

    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email, # Sending to self
            msg=f"Subject:Amazon Price Alert!\n\n{message}\nBuy now: {PRODUCT_URL}".encode("utf-8")
        )
    print("Email alert sent!")
else:
    print(f"Price is still ${price_as_float}, which is above your target of ${BUY_PRICE}.")

```