# Day 11: The Blackjack Capstone Project

Welcome to my log for Day 11! This was a big one: my first capstone project. The goal was to build a complete, text-based game of Blackjack (also known as 21). This project required me to pull together all the concepts I've learned so far, including functions with inputs and outputs, loops (`for` and `while`), conditionals (`if`/`elif`/`else`), lists, and the random module. It was a challenging but incredibly satisfying experience to see a complex game come to life.

## Table of Contents
- [1. The Goal: Building Blackjack](#1-the-goal-building-blackjack)
- [2. Deconstructing the Problem](#2-deconstructing-the-problem)
- [3. Step-by-Step Implementation](#3-step-by-step-implementation)
  - [Step 1: Dealing Cards (`deal_card` function)](#step-1-dealing-cards-deal_card-function)
  - [Step 2: Calculating Scores (`calculate_score` function)](#step-2-calculating-scores-calculate_score-function)
  - [Step 3: Handling Special Cases (Blackjack and Aces)](#step-3-handling-special-cases-blackjack-and-aces)
  - [Step 4: The Player's Turn](#step-4-the-players-turn)
  - [Step 5: The Computer's Turn](#step-5-the-computers-turn)
  - [Step 6: Determining the Winner (`compare` function)](#step-6-determining-the-winner-compare-function)
  - [Step 7: The Main Game Loop](#step-7-the-main-game-loop)
- [4. Final Project Code: Blackjack](#4-final-project-code-blackjack)

---

### 1. The Goal: Building Blackjack
The project was to create a simplified, text-based version of the card game Blackjack.  The rules are simple: get a hand of cards with a total value as close to 21 as possible without going over.
-   Cards 2-10 are their face value.
-   Jack, Queen, and King are worth 10.
-   An Ace can be worth 11 or 1.
-   Going over 21 is a "bust," and you lose immediately.

My version pits a single player against an automated computer dealer.

### 2. Deconstructing the Problem
Before writing any code, I had to break the game down into smaller, manageable pieces. This "divide and conquer" approach is a core part of programming.
1.  Deal a random card from the deck.
2.  Deal the initial two cards to both the player and the computer.
3.  Calculate the score of a given hand of cards.
4.  Handle the special case of an Ace (is it 11 or 1?).
5.  Handle the special case of a "Blackjack" (a score of 21 with the first two cards).
6.  Allow the player to "hit" (take another card) or "stand" (keep their current hand).
7.  Check if the player has busted (> 21).
8.  Implement the computer's logic (it must hit if its score is less than 17).
9.  Compare the final scores to determine the winner.
10. Ask the player if they want to play another round.

### 3. Step-by-Step Implementation

#### Step 1: Dealing Cards (`deal_card` function)
-   **What:** I created a function called `deal_card()` that returns a single random card from the deck.
-   **Why:** This encapsulates the logic for picking a card, making my code cleaner and reusable. I don't have to repeat the card-picking logic every time a card is needed.
-   **How:** I defined a list `cards` containing all possible card values (with 10 appearing four times for the 10, Jack, Queen, and King, and 11 for the Ace). The function uses `random.choice(cards)` to select and `return` one of these values.

#### Step 2: Calculating Scores (`calculate_score` function)
-   **What:** I created a `calculate_score()` function that takes a list of cards and returns their total score.
-   **Why:** This abstracts the logic for adding up card values. The rest of my program doesn't need to know *how* the score is calculated, just that it can get the score by calling this function.
-   **How:** I used the built-in `sum()` function, which is perfect for adding up all the numbers in a list. `return sum(cards)`.

#### Step 3: Handling Special Cases (Blackjack and Aces)
-   **What:** I expanded the `calculate_score()` function to handle the special rules of Blackjack.
-   **Why:** The game isn't just about summing numbers; these rules are what make it Blackjack.
-   **How:**
    -   **Blackjack:** I checked if the hand has exactly two cards and the sum is 21. If so, I returned `0` as a special value to represent a Blackjack.
    -   **Aces:** I checked if an Ace (11) is in the hand and if the total score is over 21. If both are true, I removed the 11 and appended a 1 to the list, effectively changing the Ace's value to prevent a bust. This was done using `cards.remove(11)` and `cards.append(1)`.

#### Step 4: The Player's Turn
-   **What:** I implemented the logic for the player to repeatedly choose whether to get another card ("hit").
-   **Why:** This is the core interactive part of the game for the player.
-   **How:** I used a `while` loop that continues as long as a flag variable `is_game_over` is `False`. Inside the loop, I show the player their cards and score, then ask if they want another card. If they say 'yes', I call `deal_card()` and add it to their hand. If they say 'no', I set `is_game_over` to `True` to end their turn. The loop also recalculates the score and checks for a bust or Blackjack after every card is drawn.

#### Step 5: The Computer's Turn
-   **What:** After the player's turn ends, I implemented the computer's turn.
-   **Why:** The computer needs its own logic to play against the user.
-   **How:** I used another `while` loop. This one continues as long as the computer's score is not 0 (not a Blackjack) and is less than 17. Inside the loop, the computer is forced to `deal_card()` and add it to its hand.

#### Step 6: Determining the Winner (`compare` function)
-   **What:** I created a final function, `compare()`, to check the player's and computer's final scores and determine the outcome.
-   **Why:** This centralizes all the win/loss/draw logic into one place.
-   **How:** The function takes `user_score` and `computer_score` as inputs and uses a series of `if`/`elif`/`else` statements to cover all possible outcomes (player busts, computer busts, Blackjack, higher score wins, draw, etc.) and returns a string declaring the result.

#### Step 7: The Main Game Loop
-   **What:** I wrapped the entire game logic in a `play_game()` function and used a `while` loop to ask the user if they want to play again.
-   **Why:** This allows for continuous play without having to restart the program manually.
-   **How:** The main loop checks the user's input. If they type 'y', it calls `play_game()` to start a fresh round.

---

### 4. Final Project Code: Blackjack
Here is the complete and final code for my Blackjack Capstone Project.

```python
# main.py
import random
import os
import art

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compares user and computer scores to determine the winner."""
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(art.logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
```

```python
# art.py
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
```