# Day 13: Mastering the Art of Debugging

Welcome to my log for Day 13! This day was a departure from building a single large project. Instead, I focused entirely on the crucial skill of debugging.  I've encountered plenty of bugs on my journey so far, but today I learned a structured approach to finding and fixing them. I learned that debugging isn't just about fixing errors; it's about deeply understanding how my code works.

## Table of Contents
- [1. Describe the Problem](#1-describe-the-problem)
- [2. Reproduce the Bug](#2-reproduce-the-bug)
- [3. Play Computer](#3-play-computer)
- [4. Fix Errors & Use `try`/`except`](#4-fix-errors--use-tryexcept)
- [5. Use `print()` Statements](#5-use-print-statements)
- [6. Use a Debugger](#6-use-a-debugger)
- [7. Final Debugging Tips](#7-final-debugging-tips)
- [8. Day 13 Exercises](#8-day-13-exercises)

---

### 1. Describe the Problem
The first step in fixing a bug is to clearly articulate what the problem is. If I can't explain what the code is *supposed* to do and what it's *actually* doing, I'll have a hard time fixing it.

-   **Exercise Example:** A `for` loop was intended to print a message when the iterator `i` reached 20.
    ```python
    for i in range(1, 20):
      if i == 20:
        print("You got it")
    ```
-   **Problem Description:** The loop runs from 1 up to (but not including) 20. Therefore, the condition `i == 20` is never met. My assumption that `i` would eventually become 20 was false.
-   **Fix:** Change the range to `range(1, 21)`.

---

### 2. Reproduce the Bug
Some bugs only appear under specific conditions. It's essential to find a way to make the bug happen consistently. If I can't reproduce it, I can't be sure I've fixed it.

-   **Exercise Example:** A program that picked a random number between 1 and 6 would sometimes crash with an `IndexError`.
    ```python
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = random.randint(1, 6)
    print(dice_imgs[dice_num]) # This line crashed sometimes
    ```
-   **Reproducing the Bug:** I realized the list indices are 0 through 5, but `random.randint(1, 6)` can produce the number 6. When `dice_num` was 6, the program tried to access `dice_imgs[6]`, which doesn't exist, causing the crash.
-   **Fix:** Change the random number generation to `random.randint(0, 5)`.

---

### 3. Play Computer
This technique involves mentally stepping through the code, line by line, just as a computer would. I keep track of variable values in my head or on paper to understand the program's flow and logic.

-   **Exercise Example:** Code to classify a person as a Millennial or Gen Z didn't print anything when the year 1994 was entered.
    ```python
    year = int(input("What's your year of birth?"))
    if year > 1980 and year < 1994:
      print("You are a millennial.")
    elif year > 1994:
      print("You are a Gen Z.")
    ```
-   **Playing Computer:** I traced the logic with `year = 1994`. The first `if` statement (`1994 > 1980 and 1994 < 1994`) evaluates to `True and False`, which is `False`. The `elif` statement (`1994 > 1994`) is also `False`. Neither code block ran because the year 1994 was not included in either condition.
-   **Fix:** Change one of the conditions to be inclusive, for example: `elif year >= 1994:`.

---

### 4. Fix Errors & Use `try`/`except`
Obvious errors shown by the editor (red squiggly lines) or runtime errors that crash the program should be the first priority. For runtime errors that might happen due to invalid user input, I can use a `try`/`except` block to handle them gracefully without crashing.

-   **What is it?** A `try`/`except` block allows me to "try" a piece of code that might cause an error. If an error occurs, the code in the `except` block is executed instead of the program crashing.
-   **Example:**

    ```python
    try:
        age = int(input("How old are you? "))
        print(age)
    except ValueError:
        print("You have typed an invalid number. Please enter a number.")
    ```

---

### 5. Use `print()` Statements
My best friend in debugging. Placing `print()` statements at various points in my code allows me to inspect the state of variables and understand the flow of execution. It's a simple but incredibly powerful way to see what's happening "under the hood."

---

### 6. Use a Debugger
For more complex bugs, a full-fledged debugger is the ultimate tool. I learned the basics of using the debugger in PyCharm.
-   **Breakpoints:** I can set a breakpoint on a specific line of code. When I run the program in debug mode, it will pause execution at that line. -   **Stepping Through Code:** Once paused, I can execute the code line by line ("Step Over"), allowing me to watch how variables change in real-time.
-   **Stepping Into/Out of Functions:** I can "Step Into" a function call to see what happens inside it, or "Step Out" to return to the calling code.

---

### 7. Final Debugging Tips
1.  **Take a Break:** Staring at a problem for too long can lead to tunnel vision. Stepping away often helps me see the solution clearly when I return.
2.  **Ask a Friend:** A fresh pair of eyes can spot a mistake I've been overlooking for hours.
3.  **Run Often:** I should test my code frequently as I write it, not just at the end. This helps me catch bugs right after I've introduced them.
4.  **Use Stack Overflow:** It's an invaluable resource for searching for error messages and seeing how others have solved similar problems.

---

### 8. Day 13 Exercises
This day didn't have a single final project. Instead, it was a series of small debugging challenges where I applied the techniques listed above. The goal was to practice the *process* of debugging itself. There is no final project code for this day.
  