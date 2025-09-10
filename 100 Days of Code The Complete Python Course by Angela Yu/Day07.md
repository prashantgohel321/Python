# Day 7: Project Day - Building Hangman

This is my log for Day 7. Today was a full project day where I consolidated all the skills I've learned from Day 1 to Day 6. The goal was to build the classic word-guessing game, Hangman. This project required me to use `for` and `while` loops, `if`/`else` statements, lists, strings, and modules to bring the game to life. 
## Table of Contents
- [1. Planning the Game with a Flowchart](#1-planning-the-game-with-a-flowchart)
- [2. Step 1: Setting Up the Basics](#2-step-1-setting-up-the-basics)
- [3. Step 2: Replacing Blanks with Guesses](#3-step-2-replacing-blanks-with-guesses)
- [4. Step 3: Looping for Repeated Guesses](#4-step-3-looping-for-repeated-guesses)
- [5. Step 4: Tracking Lives and Ending the Game](#5-step-4-tracking-lives-and-ending-the-game)
- [6. Step 5: Improving the User Experience](#6-step-5-improving-the-user-experience)
- [7. Final Project Code: Hangman](#7-final-project-code-hangman)

---

### 1. Planning the Game with a Flowchart
Before writing any code, I first planned the game's logic using a flowchart. This was a crucial step to break down the complex problem into smaller, manageable parts.

The basic flow is:
1.  **Start**: Generate a random word and create a list of blanks (`_`) for each letter.
2.  **User Guess**: Ask the user to guess a letter.
3.  **Check Letter**: Is the guessed letter in the word?
    -   **Yes**: Replace the corresponding blank(s) with the letter. Then, check if all blanks are filled.
        -   If all blanks are filled, the user wins. Game over.
        -   If not, go back to asking for another guess.
    -   **No**: The user loses a life. Then, check if they have any lives left.
        -   If they have no lives left, the user loses. Game over.
        -   If they still have lives, go back to asking for another guess.

---

### 2. Step 1: Setting Up the Basics
The first coding step was to get the fundamental mechanics working.
-   **Random Word Selection**: I used `random.choice()` to pick a random word from a predefined list.
-   **Get User Input**: I prompted the user to guess a letter and stored their input. I also converted their guess to lowercase using `.lower()` to make comparisons easier, since all the words in my word list were lowercase.
-   **Check the Guess**: I used a `for` loop to iterate through each `letter` in the `chosen_word` and an `if` statement to check if `letter == guess`.

---

### 3. Step 2: Replacing Blanks with Guesses
This step was about creating the visual display for the user.
-   **Create the Display**: I created a list called `display`.
-   **Populate with Blanks**: I looped through the `chosen_word` and for each letter, I added an underscore `_` to the `display` list.
-   **Replace Blanks**: I then created a second loop that iterated through the `chosen_word` using `range(len(chosen_word))`. Inside the loop, I checked if the letter at the current `position` matched the user's `guess`. If it did, I updated the `display` list at that same `position` with the guessed letter.

```python
# If the chosen_word was "apple" and the user guessed "p"
display = ["_", "_", "_", "_", "_"]
# After the loop:
display = ["_", "p", "p", "_", "_"]
```
I also learned to print the list as a string for a cleaner look using `print(" ".join(display))`.

---

### 4. Step 3: Looping for Repeated Guesses
A single guess isn't a game, so I needed to let the user guess until the game was over.
-   **`while` Loop**: I wrapped the guessing logic inside a `while` loop. The loop continues as long as a condition is met.
-   **End Condition**: I set the loop to continue as long as there were still blanks (`_`) in the `display` list. The condition was `while "_" in display:`. Once all blanks are gone, the loop terminates, and the user wins.

---

### 5. Step 4: Tracking Lives and Ending the Game
This step introduced the "Hangman" part of the game—the risk of losing.
-   **`lives` Variable**: I created a variable called `lives` and initialized it to `6`.
-   **Handling Incorrect Guesses**: I added an `if` statement: `if guess not in chosen_word:`. If a guess was incorrect, I decremented the `lives` variable by one (`lives -= 1`).
-   **Displaying ASCII Art**: I had a list of ASCII art strings called `stages`. The art was ordered from the full gallows (index 6) to the fully hung man (index 0). I used the `lives` variable as the index to print the correct stage after each guess: `print(stages[lives])`.
-   **Losing Condition**: Inside the "incorrect guess" block, I added another check: `if lives == 0:`. If true, I printed "You lose" and ended the game.

---

### 6. Step 5: Improving the User Experience
The final step was to clean up the code and make the game more user-friendly.
-   **Modularizing Code**: I moved the `word_list`, `stages`, and the game's `logo` into separate Python files (`hangman_words.py` and `hangman_art.py`). I then used `import` statements to bring them into my main script. This made my main file much cleaner.
-   **User Feedback**:
    -   I added a check to see if the user had already guessed a letter and printed a message to inform them, without penalizing a life.
    -   When a user guessed a wrong letter, I explicitly printed which letter they guessed and that it wasn't in the word.
-   **Clearing the Screen**: For a better terminal experience, I could import the `os` module and use `os.system('cls')` (for Windows) or `os.system('clear')` (for Mac/Linux) to clear the console after each guess, though this wasn't part of the core lesson.

---

### 7. Final Project Code: Hangman
Here is the complete and final code for my Hangman game.

```python
# main.py
import random
import hangman_art
import hangman_words
import os

# Function to clear the console screen
def clear():
    # For windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

# Choose a random word from the word list
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import and print the game logo
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear() # Clear the screen after each guess

    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the hangman ASCII art
    print(hangman_art.stages[lives])

```

```python
# hangman_words.py
word_list = [
'abruptly', 
'absurd', 
'abyss', 
# ... more words
'zombie', 
]
```

```python
# hangman_art.py
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    
'''
```