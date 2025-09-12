# Day 25: Working with CSV Data and the Pandas Library

Welcome to my log for Day 25! Today was a deep dive into handling and analyzing data, a core skill in Python. I started by learning how to work with CSV (Comma-Separated Values) files using Python's built-in `csv` library. Then, I was introduced to **Pandas**, a game-changing library that simplifies data manipulation and analysis. The day's project was to build an educational U.S. States guessing game, putting my new data handling skills to the test.


## Table of Contents
- [1. Working with CSV Files](#1-working-with-csv-files)
- [2. Introduction to the Pandas Library](#2-introduction-to-the-pandas-library)
- [3. DataFrames and Series](#3-dataframes-and-series)
- [4. Project: The U.S. States Game](#4-project-the-us-states-game)
- [5. Final Project Code](#5-final-project-code)

---

### 1. Working with CSV Files
My journey began with the traditional way of handling CSVs in Python.

-   **The `csv` Module:** I used the built-in `csv` module to read the `weather_data.csv` file. The `csv.reader()` function allowed me to loop through the file row by row.
-   **Manual Data Extraction:** While this worked, I quickly saw its limitations. I had to manually skip the header row and convert data types (like temperature strings) into integers. It was functional but cumbersome, especially for larger datasets.

```python
# The "old" way using the csv module
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
```

---

### 2. Introduction to the Pandas Library
This is where everything changed. Pandas is a powerful, open-source library designed for data manipulation and analysis. It makes working with tabular data (like spreadsheets or CSVs) incredibly intuitive and efficient.

-   **Installation:** Since it's not a built-in library, I first had to install it in my project's environment.
-   **Reading CSVs with Pandas:** With Pandas, reading a CSV file and loading it into a structured format takes just one line of code.

```python
import pandas

data = pandas.read_csv("weather_data.csv")
```

This single line automatically identifies headers, organizes the data, and provides a beautifully formatted table.

---

### 3. DataFrames and Series
Pandas has two core data structures that I learned about:

-   **DataFrame:** This is the main object, representing the entire table or spreadsheet. It's a 2-dimensional structure with labeled rows and columns.
-   **Series:** This represents a single column from a DataFrame. It's essentially a 1-dimensional labeled array.

Accessing data became incredibly simple:
-   **Get a Column (Series):** I could get a column of data just by treating the column header as an attribute or a dictionary key.
    ```python
    # Both of these lines get the 'temp' column
    temps = data.temp
    temps = data["temp"]
    ```
-   **Get a Row:** I could filter the DataFrame based on a condition to get a specific row.
    ```python
    # Get the row where the day is "Monday"
    monday_data = data[data.day == "Monday"]
    ```
-   **Built-in Analysis:** Pandas Series come with powerful built-in methods for data analysis, saving me from writing manual loops.
    ```python
    # Calculate the average temperature
    average_temp = data.temp.mean()
    # Find the maximum temperature
    max_temp = data.temp.max()
    ```

---

### 4. Project: The U.S. States Game
The project was to create a game that quizzes the user on the 50 states of the U.S.

-   **The Goal:** Display a blank map of the U.S. and prompt the user to type in the name of a state. If the guess is correct, the state's name is written onto the map at its correct location. The game continues until all 50 states are guessed or the user types "exit".

-   **My Process:**
    1.  **Screen Setup:** I used the `turtle` module to create the screen and set the `blank_states_img.gif` as its background shape.
    2.  **Reading State Data:** I used `pandas.read_csv()` to load `50_states.csv` into a DataFrame. This file contained three columns: `state`, `x`, and `y`.
    3.  **Game Loop:** The core of the game was a `while` loop that continued as long as the user had not guessed all 50 states.
    4.  **User Input:** Inside the loop, `screen.textinput()` prompted the user for a state name. I used `.title()` to format their answer correctly (e.g., "ohio" -> "Ohio").
    5.  **Checking the Answer:** I checked if the user's answer existed in the 'state' column of my DataFrame.
    6.  **Placing the State Name:** If the guess was correct, I filtered the DataFrame to get the row for that state, extracted the `x` and `y` coordinates, and used a new `turtle` object to write the state's name at that location on the map.
    7.  **Generating a "To-Learn" List:** If the user typed "exit", the loop would break, and the program would generate a new CSV file (`states_to_learn.csv`) containing all the states they had missed. This required me to compare the list of all states with the list of correctly guessed states.

---

### 5. Final Project Code

```python
# main.py
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

```