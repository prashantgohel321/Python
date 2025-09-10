# Day 9: Dictionaries, Nesting, and the Secret Auction

Welcome to my log for Day 9! Today was all about a new data structure: the Python Dictionary. It's a fantastic way to store related pieces of information. I learned the syntax for creating dictionaries, how to access and modify their data, and how to loop through them. I also explored the concept of "nesting" lists and dictionaries to handle more complex data. To put it all into practice, I built a Secret Auction program that takes bids from multiple users and determines the winner.

## Table of Contents
- [1. Python Dictionaries](#1-python-dictionaries)
  - [What is a Dictionary?](#what-is-a-dictionary)
  - [Retrieving, Adding, and Editing Items](#retrieving-adding-and-editing-items)
  - [Looping Through a Dictionary](#looping-through-a-dictionary)
- [2. Nesting Lists and Dictionaries](#2-nesting-lists-and-dictionaries)
- [3. Day 9 Project: Secret Auction Program](#3-day-9-project-secret-auction-program)
- [4. Final Project Code: Secret Auction](#4-final-project-code-secret-auction)

---

### 1. Python Dictionaries

#### What is a Dictionary?
-   **What is it?** A dictionary is a data structure that stores data in **key-value pairs**. It's like a real-world dictionary where you look up a word (the *key*) to find its definition (the *value*).
-   **Why do I use it?** It's extremely useful for grouping and tagging related information. Instead of just having a list of items, I can associate each item with a meaningful key.
-   **How do I create one?** I use curly braces `{}`. Each entry consists of a key, followed by a colon `:`, and then its corresponding value. Entries are separated by commas.

```python
# A dictionary with String keys and String values
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}
```

#### Retrieving, Adding, and Editing Items
-   **Retrieving:** To get a value, I access the dictionary by its key using square brackets `[]`. If I try to access a key that doesn't exist, I'll get a `KeyError`.

    ```python
    print(programming_dictionary["Bug"])
    ```

-   **Adding a New Item:** I can add a new key-value pair to the dictionary with a similar syntax.

    ```python
    programming_dictionary["Loop"] = "The action of doing something over and over again."
    ```

-   **Editing an Existing Item:** The exact same syntax is used to edit the value of an existing key. Python will find the key and overwrite its value.

    ```python
    programming_dictionary["Bug"] = "A moth in your computer."
    ```

-   **Creating an Empty Dictionary:** Sometimes it's useful to start with an empty dictionary and add to it later.

    ```python
    empty_dictionary = {}
    ```

#### Looping Through a Dictionary
When I use a `for` loop on a dictionary, it iterates through the **keys** by default. To get the value, I have to use the key inside the loop to access the dictionary.

```python
for key in programming_dictionary:
  print(key)  # This will print "Bug", then "Function", then "Loop"
  print(programming_dictionary[key]) # This will print the corresponding value
```

---

### 2. Nesting Lists and Dictionaries
Nesting is the idea of putting one data structure inside another. This allows me to model more complex, real-world data.

-   **Nesting a List in a Dictionary**: The value for a key can be a list. This is great for when a single key is associated with multiple items.

    ```python
    travel_log = {
      "France": ["Paris", "Lille", "Dijon"],
      "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    }
    ```

-   **Nesting a Dictionary in a Dictionary**: A value can also be another dictionary, creating layers of structured data.

    ```python
    travel_log = {
      "France": {"cities_visited": ["Paris", "Lille"], "total_visits": 12},
      "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 5},
    }
    ```

-   **Nesting a Dictionary in a List**: I can also have a list where each item is a dictionary. This is very common and powerful for storing a collection of similar but distinct records.

    ```python
    travel_log = [
      {
        "country": "France", 
        "cities_visited": ["Paris", "Lille"], 
        "total_visits": 12
      },
      {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 5
      },
    ]
    ```

---

### 3. Day 9 Project: Secret Auction Program
The project for the day was to build a silent auction program where bidders can enter their names and bids without others seeing them. 
The logic I followed was:
1.  Display a logo and welcome message.
2.  Create an empty dictionary called `bids` to store the data.
3.  Use a `while` loop to allow multiple people to bid.
4.  Inside the loop, ask for the user's `name` and their `bid`.
5.  Add the `name` as the key and the `bid` as the value to the `bids` dictionary.
6.  Ask if there are any other bidders. If 'yes', clear the console screen and continue the loop. If 'no', exit the loop.
7.  Once the loop is finished, create a function `find_highest_bidder()` that takes the `bids` dictionary as input.
8.  Inside this function, loop through the dictionary to find the person with the highest bid. I kept track of the highest bid seen so far and the name of the winner in separate variables.
9.  After the loop, the function prints out the winner's name and their bid amount.

---

### 4. Final Project Code: Secret Auction
Here is the complete and final code for my Secret Auction program.

```python
# main.py
import os
import art

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

print(art.logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
```

```python
# art.py
logo = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
```