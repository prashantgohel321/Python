# Day 48: Selenium WebDriver & Game Playing Bot

Welcome to my log for Day 48! This was a big step up from static scraping. Today, I learned how to use **Selenium WebDriver**, a powerful browser automation tool. Unlike `requests` and `BeautifulSoup`, which only download the static HTML of a page, Selenium can control a live browser, allowing it to interact with JavaScript, fill out forms, click buttons, and scrape dynamically loaded content.

The main project was to scrape upcoming events from Python.org, and as a fun challenge, I also started building a bot to play a simple cookie clicker game.

## Table of Contents
- [1. What is Selenium and Why Use It?](#1-what-is-selenium-and-why-use-it)
- [2. Setting up Selenium and ChromeDriver](#2-setting-up-selenium-and-chromedriver)
- [3. Finding and Interacting with Elements](#3-finding-and-interacting-with-elements)
- [4. Project: Scraping Upcoming Python Events](#4-project-scraping-upcoming-python-events)
- [5. Day 48 Project: Python.org Scraper Code](#5-day-48-project-pythonorg-scraper-code)

---

### 1. What is Selenium and Why Use It?
Selenium is a tool that automates web browsers. It's primarily used for testing web applications, but it's also incredibly useful for web scraping.

Key advantages over BeautifulSoup:
-   **JavaScript Execution:** Selenium can handle sites that rely heavily on JavaScript to load content. It waits for the content to render before scraping.
-   **User Interaction:** It can simulate user actions like clicking buttons, typing in fields, and submitting forms.
-   **Complex Navigation:** It can navigate through complex login screens or multi-step processes.

The downside is that it's slower than `requests` because it has to open and control a full browser window.

---

### 2. Setting up Selenium and ChromeDriver
To use Selenium, you need two main components:
1.  **The Selenium Python Library:** Installed via pip: `pip install selenium`.
2.  **A WebDriver:** This is a separate executable that acts as a bridge between your script and the browser. Each browser has its own WebDriver (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox).

A crucial part of the setup is ensuring the WebDriver version matches the browser version. The transcript recommended using the `webdriver-manager` library (`pip install webdriver-manager`), which automatically downloads and manages the correct ChromeDriver version, saving a lot of hassle.

```python
# No more manual driver management!
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

---

### 3. Finding and Interacting with Elements
Selenium provides various methods to locate elements on a webpage, which are imported from `selenium.webdriver.common.by.By`.

The main methods are:
-   `driver.find_element(By.ID, "some-id")`
-   `driver.find_element(By.NAME, "some-name")`
-   `driver.find_element(By.CLASS_NAME, "some-class")`
-   `driver.find_element(By.CSS_SELECTOR, "div a")`
-   `driver.find_element(By.XPATH, "/html/body/div/a[1]")`
-   `driver.find_element(By.LINK_TEXT, "Click Here")`
-   `driver.find_element(By.TAG_NAME, "h1")`

There are also plural versions (`find_elements`) that return a list of all matching elements. Once an element is found, you can get its text with `.text` or attributes with `.get_attribute('href')`.

---

### 4. Project: Scraping Upcoming Python Events
The goal was to go to `python.org` and extract the list of upcoming events from the "Upcoming Events" widget. The final output needed to be a nested dictionary containing the date and name of each event.

The steps were:
1.  **Initialize the WebDriver** and open `https://www.python.org/`.
2.  **Locate the Events Widget:** I used the CSS selector to find the `div` containing the events list (`.event-widget`).
3.  **Find All Event Times and Names:** Within that widget, I used `find_elements` to get a list of all the `<time>` elements (for dates) and another list of all the `<a>` elements (for event names).
4.  **Combine the Data:** I looped through these lists and created a dictionary for each event, then added it to a main dictionary, using an index as the key.

The final data structure looked like this:
```python
{
    0: {'time': '2024-10-25', 'name': 'PyCon ES 2024'},
    1: {'time': '2024-11-14', 'name': 'Pyjamas Conf 2024'},
    # ... and so on
}
```
Finally, the script closes the browser using `driver.quit()`.

---

### 5. Day 48 Project: Python.org Scraper Code
Here is the final code for the project.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver using webdriver-manager to handle chromedriver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the target website
driver.get("[https://www.python.org/](https://www.python.org/)")

# Find the upcoming events widget
events_widget = driver.find_element(By.CSS_SELECTOR, ".event-widget")

# Find all the time and name elements within the widget
event_times = events_widget.find_elements(By.TAG_NAME, "time")
event_names = events_widget.find_elements(By.CSS_SELECTOR, ".menu a")

# Create a dictionary to store the events
events = {}

# Loop through the found elements and populate the dictionary
for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].get_attribute("datetime").split("T")[0],
        "name": event_names[i].text,
    }

print(events)

# Close the browser session
driver.quit()

```