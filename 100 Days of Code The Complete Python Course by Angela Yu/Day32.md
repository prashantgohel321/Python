# Day 32: Sending Email (SMTP) and Managing Dates (datetime)

Welcome to my log for Day 32! This was a dive into some very practical and powerful Python modules. I learned how to send emails programmatically using the Simple Mail Transfer Protocol (SMTP) with Python's built-in `smtplib` library. I also learned how to work with dates and times using the `datetime` module. Combining these skills, I built a fantastic final project: an automated birthday emailer!


## Table of Contents
- [1. Sending Email with `smtplib`](#1-sending-email-with-smtplib)
- [2. Working with Dates & Times with `datetime`](#2-working-with-dates--times-with-datetime)
- [3. Project: The Automated Birthday Wisher](#3-project-the-automated-birthday-wisher)
- [4. Automating the Script in the Cloud](#4-automating-the-script-in-the-cloud)
- [5. Final Project Code](#5-final-project-code)

---

### 1. Sending Email with `smtplib`
This module allows my Python script to act as an email client, connecting to a mail server to send messages.

-   **What is it?** `smtplib` is Python's built-in library for sending emails using the Simple Mail Transfer Protocol (SMTP).
-   **Why do I use it?** It's essential for any application that needs to send notifications, reports, or any kind of automated email.
-   **How do I use it?** The process follows a few key steps:
    1.  **Create a connection:** I establish a connection to the email provider's SMTP server (e.g., `smtp.gmail.com`). The `with` statement is great here as it handles closing the connection automatically.
    2.  **Secure the connection:** I call `.starttls()` (Transport Layer Security) to encrypt the email, making the connection secure.
    3.  **Login:** I use `.login(user="my_email", password="my_password")` to authenticate with the email server.
    4.  **Send the email:** The `.sendmail()` method sends the message. It requires the `from_addr`, `to_addrs`, and the `msg` itself.
    5.  **Important Note on Security:** Most modern email providers (like Gmail and Yahoo) block login attempts from less secure apps by default. To make this work, I had to enable 2-Step Verification and then generate a specific **App Password** to use in my script instead of my regular account password.
    6.  **Formatting the Message:** To include a subject line, the message string must start with `Subject: Your Subject Here\n\n` followed by the body of the email.

```python
import smtplib

my_email = "my_email@gmail.com"
password = "my_app_password" # Not my real password!

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
```

---

### 2. Working with Dates & Times with `datetime`
This module provides classes for working with dates and times in a simple and powerful way.

-   **What is it?** A built-in Python module for date and time manipulation.
-   **Why do I use it?** To get the current date, compare dates, or create specific date objects for scheduling and logic.
-   **How do I use it?**
    -   **Get Current Time:** `datetime.now()` returns a `datetime` object with the current year, month, day, hour, etc.
    -   **Access Components:** I can access individual parts of the `datetime` object, like `now.year`, `now.month`, or `now.weekday()` (which returns a number, with Monday being 0).
    -   **Create a Date:** I can create my own `datetime` object by providing the year, month, and day: `dt.datetime(year=1995, month=12, day=15)`.

---

### 3. Project: The Automated Birthday Wisher
The capstone project for the day was to create a program that automatically sends a happy birthday email to friends and family.

-   **My Process:**
    1.  **Check the Date:** The first step was to get today's month and day using `datetime.now()`. I stored this as a tuple, like `(7, 14)`.
    2.  **Read Birthdays:** I used `pandas` to read a `birthdays.csv` file. This file contains columns for `name`, `email`, `year`, `month`, and `day`.
    3.  **Create a Birthday Dictionary:** The most efficient way to check for birthdays was to convert the Pandas DataFrame into a dictionary. I used a dictionary comprehension with `.iterrows()` to create a dictionary where the keys were `(month, day)` tuples and the values were the corresponding row of data for each person.
    4.  **Check for a Match:** I then checked if the tuple for today's date existed as a key in my birthday dictionary.
    5.  **Personalize and Send:** If a match was found:
        -   I randomly selected one of three pre-written letter templates from a folder.
        -   I read the content of the template file.
        -   I used the `.replace()` string method to replace the `[NAME]` placeholder with the person's name from the birthday data.
        -   Finally, I used `smtplib` to send this newly created, personalized email to the person's email address.

---

### 4. Automating the Script in the Cloud
A script like this is only useful if it runs automatically every day.

-   **PythonAnywhere:** I learned about cloud services like PythonAnywhere that can host and run Python scripts on a schedule.
-   **Process:** I uploaded my project files (`main.py`, `birthdays.csv`, and the letter templates folder), and then set up a scheduled task to run my `main.py` script once every day. This way, the program checks for birthdays automatically without my computer even needing to be on.

---

### 5. Final Project Code

```python
# main.py
import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "YOUR_EMAIL@gmail.com"
MY_PASSWORD = "YOUR_APP_PASSWORD"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
```