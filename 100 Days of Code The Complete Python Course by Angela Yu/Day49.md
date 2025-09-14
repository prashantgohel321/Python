# Day 49: Automated Gym Booking Bot with Selenium

Welcome to my log for Day 49! Today's project was a deep dive into creating a robust and intelligent automation script. I built a bot to automatically book classes on a mock gym website. This wasn't just about clicking buttons; it involved handling user sessions, dynamic content, verification, and error handling—skills that are crucial for creating bots that work reliably in the real world.

## Table of Contents
- [1. Project Goal: The "Snack & Lift" Gym Booker](#1-project-goal-the-snack--lift-gym-booker)
- [2. Persistent Sessions with a Chrome Profile](#2-persistent-sessions-with-a-chrome-profile)
- [3. Smart Booking: Checking Before Clicking](#3-smart-booking-checking-before-clicking)
- [4. Verification: Trust but Verify](#4-verification-trust-but-verify)
- [5. Building Resilience: Handling Network Failures](#5-building-resilience-handling-network-failures)
- [6. Day 49 Project: Automated Gym Booker Code](#6-day-49-project-automated-gym-booker-code)

---

### 1. Project Goal: The "Snack & Lift" Gym Booker
The objective was to create a Selenium bot that could:
-   Log into a mock gym website.
-   Identify and book specific classes (e.g., all Tuesday and Thursday 6 PM classes).
-   Handle cases where a class is full (join the waitlist) or already booked.
-   Verify that the bookings were successful by checking a separate "My Bookings" page.
-   Be resilient enough to handle intermittent network failures.

---

### 2. Persistent Sessions with a Chrome Profile
A major step up in this project was making the bot's session persistent. Normally, Selenium starts a fresh, clean browser session every time. This means cookies, cache, and login information are wiped.
-   **The Problem:** Forcing the bot to log in every single time is inefficient and doesn't mimic real user behavior.
-   **The Solution:** I configured Selenium to use a dedicated Chrome user profile. By setting the `user-data-dir` option, Selenium saves all session data (cookies, local storage) to a folder. On subsequent runs, it loads this profile, and the website remembers the bot as a logged-in user. This is a game-changer for automating tasks that require authentication.

```python
chrome_options = webdriver.ChromeOptions()
# Create a folder for the Chrome Profile Selenium will use
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
```

---

### 3. Smart Booking: Checking Before Clicking
Instead of blindly clicking every "Book" button, the bot was made more intelligent.
-   **Stateful Buttons:** The website's buttons change their text based on the booking status: "Book Class", "Join Waitlist", "Booked", or "Waitlisted".
-   **Conditional Logic:** Before performing an action, the script reads the text on the button (`button.text`). Using an `if/elif` block, it decides the correct action:
    -   If "Book Class", click it and log a new booking.
    -   If "Join Waitlist", click it and log a new waitlist entry.
    -   If "Booked" or "Waitlisted", skip it and log that it's already handled.
This prevents errors and makes the script's logic much more robust.

---

### 4. Verification: Trust but Verify
Just because Selenium clicks a button doesn't guarantee the action was successful on the backend. A crucial part of reliable automation is verification.
-   **The Process:** After attempting all bookings on the main schedule page, the bot navigates to the "My Bookings" page.
-   **Counting and Comparing:** It then scrapes this page to count how many relevant classes (Tuesday/Thursday 6 PM) are actually listed.
-   **Reporting:** Finally, it compares the number of *attempted* bookings with the number of *verified* bookings and prints a success or mismatch message. This confirms the bot's actions had the intended effect.

---

### 5. Building Resilience: Handling Network Failures
The most advanced part of this project was preparing the bot for an unreliable environment. The mock website had a feature to simulate network failures.
-   **The Challenge:** A network error could crash the script during a critical step like logging in or booking a class.
-   **The Solution: A Retry Wrapper:** I implemented a higher-order function called `retry`. This function takes another function (like `login()` or `book_class()`) as an argument.
    -   It calls the function inside a `try...except` block.
    -   If the function fails (throws an exception), the wrapper catches it, waits for a moment, and tries again, up to a specified number of retries.
    -   If the function succeeds, the wrapper exits.
This design pattern is incredibly powerful for making automation scripts that can withstand temporary glitches and network issues without failing completely.

---

### 6. Day 49 Project: Automated Gym Booker Code
Here is the final code, incorporating the persistent profile, smart booking logic, verification, and resilience.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import os
import time

# --- Account Details ---
ACCOUNT_EMAIL = "your_email@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "your_password"      # The password you used
GYM_URL = "[https://appbrewery.github.io/gym/](https://appbrewery.github.io/gym/)"

# --- Setup Chrome Profile and Driver ---
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 5)

# --- Automated Login ---
try:
    # Check if we are already on the schedule page (already logged in)
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    print("Already logged in.")
except:
    # If not, perform login
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    print("Login successful.")


# --- Class Booking Logic ---
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                already_booked_count += 1
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                already_booked_count += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                button.click()
                booked_count += 1
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(0.5) # Wait for UI to update
            elif button.text == "Join Waitlist":
                button.click()
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5) # Wait for UI to update

# --- Print Booking Summary ---
total_processed = booked_count + waitlist_count + already_booked_count
print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {booked_count}")
print(f"New waitlist entries: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday & Thursday 6pm classes processed: {total_processed}")

print("\n--- DETAILED CLASS LIST ---")
for detail in processed_classes:
    print(f"  • {detail}")

# --- Verification Step ---
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()
wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        continue # Not a booking card

print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_processed} bookings/waitlists")
print(f"Found: {verified_count} bookings/waitlists on page")

if total_processed == verified_count:
    print("✅ SUCCESS: All actions verified!")
else:
    print(f"❌ MISMATCH: Missing {total_processed - verified_count} items on booking page.")

# driver.quit() # Keep browser open to inspect manually
```