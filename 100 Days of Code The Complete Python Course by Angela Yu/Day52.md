# Day 52: Instagram Follower Bot

Welcome to my log for Day 52! Today’s project was to build an **Instagram Follower Bot**. The strategy is simple: find a popular account with a similar audience to the one you want to build, and then systematically follow their followers. The idea is that a percentage of these users will notice the follow and follow you back, helping to grow your account's presence.

This was an excellent Selenium challenge that involved dealing with dynamically loaded content, scrolling inside a modal pop-up, and handling various interruptions.

## Table of Contents
- [1. Project Goal: The InstaFollower Bot](#1-project-goal-the-instafollower-bot)
- [2. Step 1: Logging into Instagram](#2-step-1-logging-into-instagram)
- [3. Step 2: Finding and Scrolling Through Followers](#3-step-2-finding-and-scrolling-through-followers)
- [4. Step 3: Following and Handling Exceptions](#4-step-3-following-and-handling-exceptions)
- [5. Day 52 Project: Instagram Follower Bot Code](#5-day-52-project-instagram-follower-bot-code)

---

### 1. Project Goal: The InstaFollower Bot
The goal was to create a bot that could:
1.  Log in to a specified Instagram account.
2.  Navigate to the page of a target account (e.g., a competitor or influencer in the same niche).
3.  Open the list of that account's followers.
4.  Scroll through the list to load more users.
5.  Click the "Follow" button for each user in the list.

The entire process was structured within an `InstaFollower` class to keep the code organized.

---

### 2. Step 1: Logging into Instagram
The first task was automating the login process.
-   **Navigation:** The bot opens the Instagram login page.
-   **Dismissing Pop-ups:** Instagram presents a cookie consent dialog and, after login, prompts to save login info and turn on notifications. The bot handles these by finding buttons containing specific text (like "Not now") using a flexible XPath, as the exact selectors can be dynamic.
-   **Credentials:** The bot enters the username and password into the respective fields and submits the form to log in.

---

### 3. Step 2: Finding and Scrolling Through Followers
This was the most challenging part of the project.
-   **Accessing the List:** After logging in, the bot navigates directly to the followers page of the target account (e.g., `https://www.instagram.com/chefsteps/followers`).
-   **The Modal Pop-up:** The list of followers appears in a modal pop-up window. This list only shows a small number of followers initially; more are loaded as you scroll down *within the modal itself*.
-   **Executing JavaScript for Scrolling:** A standard Selenium scroll won't work here. The solution was to use `driver.execute_script()`. I located the modal element and then passed it into a JavaScript command that sets the modal's `scrollTop` to its `scrollHeight`, effectively scrolling it to the bottom. This was repeated in a loop to load hundreds of followers.

```javascript
// The JavaScript executed by Selenium
"arguments[0].scrollTop = arguments[0].scrollHeight"
```

---

### 4. Step 3: Following and Handling Exceptions
With the list of followers loaded, the final step was to iterate through them and click "Follow".
-   **Finding Buttons:** The bot selects all the "Follow" buttons within the modal.
-   **The Loop:** It then loops through each button and clicks it, with a short `time.sleep()` to appear more human and avoid being rate-limited.
-   **Exception Handling:** What if the bot tries to follow an account that is *already* being followed? Instagram will show a confirmation pop-up asking to "Unfollow". This action covers the next "Follow" button, leading to an `ElementClickInterceptedException`. The `try...except` block catches this, finds the "Cancel" button on the unfollow pop-up, clicks it, and continues to the next person in the list.

---

### 5. Day 52 Project: Instagram Follower Bot Code
Here is the final code for the Instagram Follower Bot.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

# --- Your Details ---
SIMILAR_ACCOUNT = "chefsteps"  # The account whose followers you want to target
INSTAGRAM_USERNAME = os.environ.get("INSTA_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTA_PASSWORD")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        """Logs into Instagram and handles initial pop-ups."""
        self.driver.get("[https://www.instagram.com/accounts/login/](https://www.instagram.com/accounts/login/)")
        time.sleep(5)

        # Handle cookie pop-up
        try:
            decline_cookies_button = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
            if decline_cookies_button:
                decline_cookies_button.click()
                time.sleep(1)
        except:
            print("Cookie pop-up not found, continuing.")

        username_input = self.driver.find_element(by=By.NAME, value="username")
        password_input = self.driver.find_element(by=By.NAME, value="password")
        username_input.send_keys(INSTAGRAM_USERNAME)
        password_input.send_keys(INSTAGRAM_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # Handle "Save your login info?" pop-up
        try:
            not_now_button = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
            if not_now_button:
                not_now_button.click()
                time.sleep(2)
        except:
            print("Save login pop-up not found.")
        
        # Handle "Turn on Notifications" pop-up
        try:
            not_now_notifications = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
            if not_now_notifications:
                not_now_notifications.click()
                time.sleep(2)
        except:
            print("Notifications pop-up not found.")

    def find_followers(self):
        """Navigates to the target account's followers and scrolls to load them."""
        self.driver.get(f"[https://www.instagram.com/](https://www.instagram.com/){SIMILAR_ACCOUNT}/followers")
        time.sleep(8)
        
        # Note: This XPATH might be fragile and change over time.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        
        print("Scrolling through followers...")
        for i in range(10):  # Scroll 10 times to load a good number of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        """Finds and clicks all 'Follow' buttons, handling exceptions."""
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
        
        for button in all_buttons:
            try:
                if button.text == "Follow":
                    button.click()
                    print("Followed a user.")
                    time.sleep(1.5) # Pause to avoid being blocked
            except ElementClickInterceptedException:
                # This happens if you try to follow someone you already are.
                # A pop-up appears, so we cancel it.
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                print("Already following, cancelled.")
                time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

print("Finished following session.")
```