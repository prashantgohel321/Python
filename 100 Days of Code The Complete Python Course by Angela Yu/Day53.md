# Day 53: Data Entry Automation Capstone Project

Welcome to the capstone project for the web scraping section! Day 53 was all about combining the skills I've learned—using both **BeautifulSoup** and **Selenium**—to automate a common real-world task: data entry. The project simulates a job where I need to find rental property listings that meet specific criteria, scrape the relevant information, and enter it into a spreadsheet.

This project was a comprehensive test of my ability to parse web data, clean it, and use browser automation to interact with forms.

## Table of Contents
- [1. Project Goal: Automating Property Research](#1-project-goal-automating-property-research)
- [2. Part 1: Scraping Listings with BeautifulSoup](#2-part-1-scraping-listings-with-beautifulsoup)
- [3. Part 2: Automating Data Entry with Selenium](#3-part-2-automating-data-entry-with-selenium)
- [4. Day 53 Project: Data Entry Automation Code](#4-day-53-project-data-entry-automation-code)

---

### 1. Project Goal: Automating Property Research
The objective was to create a script that automates the following workflow:
1.  **Scrape Data:** Visit a clone of a Zillow search results page for rental properties in San Francisco.
2.  **Extract Information:** Use BeautifulSoup to extract the address, price, and property link for every listing on the page.
3.  **Clean Data:** Process the extracted text to remove unwanted characters, formatting, and extra words (like "/mo" or "+").
4.  **Enter Data:** Use Selenium to open a custom Google Form.
5.  **Populate Form:** For each property listing, fill out the form with the scraped address, price, and link.
6.  **Submit:** Submit the form for each listing, creating a new entry.
The final result is a Google Sheet (generated from the form responses) that contains a clean, structured list of all the properties.

---

### 2. Part 1: Scraping Listings with BeautifulSoup
The first half of the project focused on data extraction. BeautifulSoup is perfect for this because it's fast and efficient at parsing static HTML.
-   **Making the Request:** I used the `requests` library to get the HTML content from the Zillow clone website. It was important to include headers (`User-Agent`, `Accept-Language`) to make the request look like it was coming from a real browser.
-   **Parsing with BeautifulSoup:** I created a `BeautifulSoup` object from the response text.
-   **Extracting Links, Addresses, and Prices:** I used CSS selectors to find all the relevant elements.
    -   `soup.select(".StyledPropertyCardDataWrapper a")` to get all the link (`<a>`) tags. I then used a list comprehension to extract the `href` attribute from each.
    -   `soup.select(".StyledPropertyCardDataWrapper address")` to get all the addresses.
    -   `soup.select(".PropertyCardWrapper span")` to get all the price elements.
-   **Data Cleaning:** The scraped text was messy. I used string methods like `.get_text()`, `.strip()`, `.replace()`, and `.split()` to clean up each piece of data, ensuring the final lists contained only the necessary information (e.g., "$2,500" instead of "$2,500+/mo").

---

### 3. Part 2: Automating Data Entry with Selenium
The second half of the project involved using Selenium to interact with a live website (the Google Form).
-   **Setting up the Form:** I first created a simple Google Form with three short-answer questions: "Address," "Price," and "Link."
-   **Automating Submission:**
    -   I wrote a `for` loop to iterate through the lists of addresses, prices, and links I had scraped.
    -   Inside the loop, the Selenium driver would `get()` the Google Form URL.
    -   Using their XPaths, the bot located the input fields for each question and used `.send_keys()` to fill them with the corresponding data for that listing.
    -   Finally, it located the "Submit" button and clicked it.
-   **Looping for All Listings:** This process repeated for every property found, effectively transferring all the scraped data into the form, which in turn populated the linked Google Sheet.

---

### 4. Day 53 Project: Data Entry Automation Code
Here is the final, complete code that combines both BeautifulSoup and Selenium to accomplish the task.

```python
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- Part 1: Scrape data using BeautifulSoup ---

# Zillow Clone URL with search filters applied
ZILLOW_CLONE_URL = "[https://appbrewery.github.io/Zillow-Clone/](https://appbrewery.github.io/Zillow-Clone/)"

# Headers to mimic a browser request
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(ZILLOW_CLONE_URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# Get all listing links
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]

# Get all listing addresses
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

# Get all listing prices
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]


# --- Part 2: Fill Google Form using Selenium ---

# URL for the Google Form you created
GOOGLE_FORM_URL = "YOUR_GOOGLE_FORM_LINK_HERE" # <-- IMPORTANT: PASTE YOUR FORM LINK HERE

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    # Find form fields by their XPath (you may need to update these for your form)
    address_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    
    # Fill in the form
    address_input.send_keys(all_addresses[n])
    price_input.send_keys(all_prices[n])
    link_input.send_keys(all_links[n])
    
    # Submit the form
    submit_button.click()
    print(f"Form submitted for property {n+1}.")

print("All listings have been submitted.")
driver.quit()
```