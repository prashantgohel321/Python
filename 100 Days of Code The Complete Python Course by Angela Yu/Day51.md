# Day 51: Automated Internet Speed Complaint Bot

Welcome to my log for Day 51! Today's project was about building a bot with a purpose: to automatically complain to my Internet Service Provider (ISP) when my internet speed drops below what I'm paying for. This is a fantastic real-world application of Selenium that combines browser automation, data extraction, and social media interaction.

The bot first navigates to Speedtest.net to measure the current download and upload speeds, then logs into Twitter to post a public complaint mentioning the provider if the speeds are disappointing.

## Table of Contents
- [1. Project Goal: The Internet Speed Complaint Bot](#1-project-goal-the-internet-speed-complaint-bot)
- [2. Structuring the Bot with a Class](#2-structuring-the-bot-with-a-class)
- [3. Step 1: Getting the Internet Speed](#3-step-1-getting-the-internet-speed)
- [4. Step 2: Tweeting at the Provider](#4-step-2-tweeting-at-the-provider)
- [5. Day 51 Project: Internet Speed Twitter Bot Code](#5-day-51-project-internet-speed-twitter-bot-code)

---

### 1. Project Goal: The Internet Speed Complaint Bot
Many ISPs guarantee a certain minimum internet speed, but often fail to deliver. Manually running speed tests and complaining is tedious. This project automates the entire process.

The bot will:
1.  Run an internet speed test using `speedtest.net`.
2.  Extract the download and upload speed results.
3.  Compare these speeds to the promised speeds defined in the script.
4.  If the speeds are lower, it will log in to Twitter.
5.  Compose and post a tweet that includes the poor speed results and tags the ISP.

---

### 2. Structuring the Bot with a Class
To keep the code organized and clean, the entire logic was encapsulated within a Python class called `InternetSpeedTwitterBot`.

-   **`__init__()`**: Initializes the Selenium WebDriver and sets up instance variables for the download (`self.down`) and upload (`self.up`) speeds.
-   **`get_internet_speed()`**: A method to handle all the Selenium interactions with speedtest.net.
-   **`tweet_at_provider()`**: A method to handle the Twitter login and tweet composition.

This structure makes the code easy to read and maintain, with each method having a single, clear responsibility.

---

### 3. Step 1: Getting the Internet Speed
This method automates the process of running a speed test.
-   **Navigation:** The bot opens `https://www.speedtest.net/`.
-   **Start Test:** It finds and clicks the "GO" button to begin the test.
-   **Waiting for Results:** This is a crucial step. A speed test can take anywhere from 30 seconds to a few minutes. A `time.sleep(60)` was used to give the test enough time to complete before the script tries to find the results.
-   **Scraping Results:** Once the test is done, the bot uses `find_element` with specific XPaths to locate the download and upload speed values on the results page. These values are then stored in `self.down` and `self.up`.

---

### 4. Step 2: Tweeting at the Provider
This method is triggered if the measured speeds are below the promised values.
-   **Twitter Login:** The bot navigates to Twitter's login page. It finds the email and password fields, enters the credentials (stored as constants), and submits the form. `time.sleep()` is used to handle page load times.
-   **Composing the Tweet:** After logging in, the bot finds the tweet composition box. It then constructs a formatted string containing the complaint, including the actual and promised download/upload speeds.
-   **Sending the Tweet:** Finally, it finds and clicks the "Tweet" button to post the complaint publicly.

---

### 5. Day 51 Project: Internet Speed Twitter Bot Code
Here is the final, complete code for the project.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# --- Your Details ---
PROMISED_DOWN = 150  # Your promised download speed in Mbps
PROMISED_UP = 10     # Your promised upload speed in Mbps
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Runs a speed test and saves the download/upload speeds."""
        self.driver.get("[https://www.speedtest.net/](https://www.speedtest.net/)")
        
        # Optional: Handle cookie/privacy pop-up if it appears
        # try:
        #     accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        #     accept_button.click()
        #     time.sleep(1)
        # except:
        #     print("No cookie button found.")

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        print("Running speed test. Please wait...")
        time.sleep(60)  # Wait for the test to complete
        
        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(f"Download: {self.down} Mbps")
        print(f"Upload: {self.up} Mbps")

    def tweet_at_provider(self):
        """Logs into Twitter and tweets a complaint if speeds are low."""
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            print("Internet speed is below promised values. Tweeting complaint...")
            self.driver.get("[https://twitter.com/login](https://twitter.com/login)")

            time.sleep(3)
            email_input = self.driver.find_element(By.NAME, "text")
            email_input.send_keys(TWITTER_EMAIL)
            email_input.send_keys(Keys.ENTER)
            
            time.sleep(3)
            # Twitter might ask for a username/phone number as a security check
            try:
                password_input = self.driver.find_element(By.NAME, "password")
            except:
                # Handle the case where it asks for username first
                username_input = self.driver.find_element(By.NAME, "text")
                username_input.send_keys("YourTwitterHandle") # Change this
                username_input.send_keys(Keys.ENTER)
                time.sleep(2)
                password_input = self.driver.find_element(By.NAME, "password")

            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)

            time.sleep(5)
            tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

            tweet = f"Hey @YourISP, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_compose.send_keys(tweet)
            time.sleep(2)

            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()
            print("Tweet sent successfully.")
            time.sleep(3)
            self.driver.quit()
        else:
            print("Internet speed is fine. No complaint needed.")
            self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

```