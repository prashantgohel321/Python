# Day 14: The Higher Lower Game Project

Welcome to my log for Day 14! The project for today was to build the "Higher Lower" game. More than just a coding exercise, this was a lesson in project planning and problem decomposition. Starting with a blank file, I had to analyze the final product, break it down into a list of smaller problems, and tackle them one by one. This process of turning a big, intimidating idea into a structured plan is one of the most valuable skills I'm learning.

## Table of Contents
- [1. The Project: Higher Lower Game](#1-the-project-higher-lower-game)
- [2. My Problem-Solving Approach](#2-my-problem-solving-approach)
- [3. Step-by-Step Implementation](#3-step-by-step-implementation)
  - [Step 1: Generating Random Accounts](#step-1-generating-random-accounts)
  - [Step 2: Formatting Data for Display](#step-2-formatting-data-for-display)
  - [Step 3: Checking the Answer](#step-3-checking-the-answer)
  - [Step 4: Making the Game Loop](#step-4-making-the-game-loop)
- [4. Final Project Code: Higher Lower Game](#4-final-project-code-higher-lower-game)

---

### 1. The Project: Higher Lower Game
The goal was to create a game where the user guesses which of two celebrities or brands has more Instagram followers. -   The game presents two options, 'A' and 'B'.
-   I have to guess whether 'B' has a higher follower count than 'A'.
-   If I'm right, my score increases by one, and 'B' becomes the new 'A' for the next round against a new 'B'.
-   If I'm wrong, the game ends and shows my final score.

---

### 2. My Problem-Solving Approach
This project was all about the process. Instead of just diving into code, I followed a structured plan:

1.  **Break Down the Problem:** I played the final version of the game several times to understand its mechanics and identify the core components. I listed them out as a series of smaller problems to solve.
    -   Display the logo and art.
    -   Get a random account from the data list.
    -   Format the account data into a printable string.
    -   Ask the user for their guess.
    -   Check if the user's guess is correct by comparing follower counts.
    -   Keep track of the score.
    -   Make the game repeatable.
    -   Move account B to position A after a correct guess.
    -   Clear the screen between rounds.

2.  **Create a TODO List (as Comments):** I turned my list of problems into comments in my `main.py` file. This acted as a roadmap for what I needed to build.

3.  **Tackle the Easiest Task First:** I started with simple things like importing the necessary data and art files and getting a random account. Building momentum with small wins made the bigger tasks seem less daunting.

4.  **Write Code -> Run Code -> Fix Code -> Repeat:** For each small task, I followed an iterative development cycle. I'd write a small piece of code to solve one comment, run the program to see if it worked, and fix any bugs immediately. This constant feedback loop helped me catch errors early and ensure each part was working before I built on top of it.

---

### 3. Step-by-Step Implementation

#### Step 1: Generating Random Accounts
-   **What:** I needed a way to randomly select two different accounts from the `game_data` list.
-   **Why:** This is the core mechanic that makes the game unpredictable and replayable.
-   **How:** I used `random.choice(data)` to pick a random dictionary from the list of accounts. I created one for `account_a` and another for `account_b`. I also added a simple `while` loop to ensure that `account_a` and `account_b` were never the same, re-picking `account_b` if they were.

#### Step 2: Formatting Data for Display
-   **What:** The raw data was a dictionary (e.g., `{'name': 'Instagram', 'follower_count': 346, ...}`). I needed to present this to the user in a readable sentence (e.g., "Instagram, a social media platform, from United States").
-   **Why:** Good user experience requires presenting data clearly. Abstracting this logic into a function also makes the main code cleaner.
-   **How:** I created a function `format_data(account)` that took an account dictionary as input. Inside, it accessed the values for the 'name', 'description', and 'country' keys and used an f-string to combine them into a single, formatted string, which it then returned.

#### Step 3: Checking the Answer
-   **What:** The most complex piece of logic. I needed to compare the follower counts of account A and B and determine if the user's guess ('a' or 'b') was correct.
-   **Why:** This determines whether the player wins the round or loses the game.
-   **How:** I created a function `check_answer(guess, a_followers, b_followers)`. It used an `if` statement to see which account had more followers. Based on that, it returned `True` if the user's `guess` matched the winner, and `False` otherwise. This was a neat way to simplify a potentially complex set of conditions.

#### Step 4: Making the Game Loop
-   **What:** The game needed to continue as long as the user kept guessing correctly and end when they were wrong.
-   **Why:** This creates the core game loop and win/loss conditions.
-   **How:**
    -   I used a `while` loop controlled by a boolean flag, `game_should_continue`.
    -   Inside the loop, I presented the two accounts, got the user's guess, and called `check_answer()`.
    -   If the answer was correct, I incremented the score, cleared the screen, and set `account_a` to the value of `account_b` for the next round.
    -   If the answer was wrong, I set `game_should_continue` to `False`, which caused the loop to terminate and end the game.

---

### 4. Final Project Code: Higher Lower Game
Here is the complete and final code for my Higher Lower Game project.

```python
# main.py
import random
import os
from art import logo, vs
from game_data import data

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Takes the account data and returns the printable format."""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Takes the user's guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
```

```python
# art.py
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
```

```python
# game_data.py
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    # ... more data entries
]
```