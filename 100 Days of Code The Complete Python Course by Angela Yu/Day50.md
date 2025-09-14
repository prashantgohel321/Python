# Day 50: Auto Tinder Swiping Bot

Welcome to my log for Day 50! We've hit the halfway point of the bootcamp! Today's project was a fun and practical application of Selenium: an **Auto Tinder Swiping Bot**. The idea was to automate the repetitive task of swiping right on profiles to save time and effort. This project was a great challenge, requiring me to handle multiple browser windows, deal with various pop-ups, and write resilient code that can handle unexpected interruptions.

## Table of Contents
- [1. Project Goal: Automate the Swipe](#1-project-goal-automate-the-swipe)
- [2. Step 1: The Login Flow via Facebook](#2-step-1-the-login-flow-via-facebook)
- [3. Step 2: Handling Multiple Browser Windows](#3-step-2-handling-multiple-browser-windows)
- [4. Step 3: Dismissing All Pop-ups](#4-step-3-dismissing-all-pop-ups)
- [5. Step 4: The Swiping Loop and Exception Handling](#5-step-4-the-swiping-loop-and-exception-handling)
- [6. Day 50 Project: Auto Tinder Swiper Code](#6-day-50-project-auto-tinder-swiper-code)

---

### 1. Project Goal: Automate the Swipe
The main objective was to create a Python script that uses Selenium to:
1.  Open Tinder.com.
2.  Log in using a Facebook account to bypass phone verification hassles.
3.  Dismiss the initial barrage of pop-ups (location, notifications, cookies).
4.  Automatically click the "Like" button on profiles, up to the free daily limit of 100.
5.  Handle interruptions, such as "It's a Match!" pop-ups, without crashing.

---

### 2. Step 1: The Login Flow via Facebook
Tinder's primary login can be tricky to automate due to phone number verification. A more stable approach is to use the "Login with Facebook" option. The initial steps involve navigating to Tinder's homepage, clicking the main "Log in" button, and then selecting the Facebook login option. I used `time.sleep()` between clicks to ensure the page elements had enough time to load before the script tried to interact with them.

---

### 3. Step 2: Handling Multiple Browser Windows
Clicking "Login with Facebook" opens the login form in a new, separate browser window. Selenium, by default, remains focused on the original window. To interact with the Facebook login fields, I had to explicitly switch control to the new window.
-   **Getting Window Handles:** `driver.window_handles` returns a list of all open window identifiers. The original window is at index `[0]`, and the new pop-up is at index `[1]`.
-   **Switching Windows:** I used `driver.switch_to.window(fb_login_window)` to shift Selenium's focus. After filling in the credentials and submitting the form, the pop-up closes, and it's crucial to switch the driver's focus back to the main Tinder window with `driver.switch_to.window(base_window)`.

---

### 4. Step 3: Dismissing All Pop-ups
Once logged in, Tinder presents a series of modal dialogs that must be handled before the bot can start swiping. These include requests for:
-   **Location Access:** Click "ALLOW".
-   **Notifications:** Click "NOT INTERESTED".
-   **Cookies:** Click "I ACCEPT".

I used specific XPaths to target each button and `sleep()` to wait for them to appear, ensuring the script could reliably dismiss them in order.

---

### 5. Step 4: The Swiping Loop and Exception Handling
This is the core of the bot. I created a `for` loop to run 100 times, representing the daily swipe limit. Inside the loop, the bot tries to click the "Like" button. However, two common issues can interrupt this:
-   **A Match Pop-up:** When a match occurs, a pop-up covers the "Like" button. Trying to click it would raise an `ElementClickInterceptedException`. The `except` block for this error finds and clicks the "BACK TO TINDER" link on the pop-up to dismiss it.
-   **Slow Loading:** Sometimes, a new profile hasn't loaded yet, and the "Like" button doesn't exist. This would raise a `NoSuchElementException`. The `except` block for this error simply tells the script to `sleep(2)` and wait for the page to catch up.

This `try...except` structure makes the bot robust enough to run unattended without crashing.

---

### 6. Day 50 Project: Auto Tinder Swiper Code
Here is the final, complete code for the Tinder swiping bot.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import os

# --- Your Facebook Credentials ---
# It's recommended to use environment variables for security
FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

# --- Setup Selenium Driver ---
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("[http://www.tinder.com](http://www.tinder.com)")

# --- Login Sequence ---
sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login_button.click()

# --- Switch to Facebook Login Window ---
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(f"Switched to: {driver.title}")

# --- Fill Facebook Credentials ---
email_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
password_input = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email_input.send_keys(FB_EMAIL)
password_input.send_keys(FB_PASSWORD)
password_input.send_keys(Keys.ENTER)

# --- Switch Back to Tinder Window ---
driver.switch_to.window(base_window)
print(f"Switched back to: {driver.title}")

# --- Dismiss Pop-ups ---
sleep(5) # Allow time for main page to load
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
sleep(1)
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
sleep(1)
cookies_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies_button.click()
sleep(1)

# --- Swiping Loop ---
for n in range(100):
    sleep(1.5) # Add a delay between swipes
    try:
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
        print(f"Liked person {n+1}")
    except ElementClickInterceptedException:
        try:
            # Handle "It's a Match!" pop-up
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
            print("Match pop-up dismissed.")
        except NoSuchElementException:
            # Handle other potential pop-ups if necessary
            sleep(2)
    except NoSuchElementException:
        print("Like button not found, waiting...")
        sleep(2)

print("Daily swipe limit reached.")
# driver.quit()

```