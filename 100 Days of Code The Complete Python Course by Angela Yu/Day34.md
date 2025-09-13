# Day 34: APIs & GUI - The Quizzler App

Welcome to my log for Day 34! Today was a fantastic review day where I upgraded the quiz game from Day 17 into a full-fledged GUI application called "Quizzler." This project involved pulling together several key skills: fetching dynamic data from the Open Trivia Database API, building a user interface with Tkinter, organizing the code with OOP principles, and using type hints to make the code more robust.


## Table of Contents
- [1. Project Overview: The Quizzler App](#1-project-overview-the-quizzler-app)
- [2. Fetching Questions from the Open Trivia Database API](#2-fetching-questions-from-the-open-trivia-database-api)
- [3. Structuring the UI with a Class](#3-structuring-the-ui-with-a-class)
- [4. Type Hinting and Code Safety](#4-type-hinting-and-code-safety)
- [5. Providing Instant User Feedback](#5-providing-instant-user-feedback)
- [6. Final Project Code](#6-final-project-code)

---

### 1. Project Overview: The Quizzler App
The goal was to transform the console-based quiz into an interactive GUI application.
-   **Dynamic Questions:** Instead of a fixed list, the app fetches 10 new true/false questions from the Open Trivia Database API every time it runs.
-   **GUI:** The interface, built with Tkinter, displays the score, the current question on a canvas, and true/false buttons for the user to click.
-   **OOP Structure:** The app's logic is cleanly separated into different classes: `Question`, `QuizBrain` for game logic, and a new `QuizInterface` for the UI.

---

### 2. Fetching Questions from the Open Trivia Database API
To make the quiz endlessly replayable, I needed to get new questions from an external source.

-   **Making the API Call:** I used the `requests` library to make a `GET` request to the API endpoint.
-   **Using Parameters:** I passed parameters to the API to customize the data I received. Specifically, I requested `amount=10` and `type=boolean` to get ten true/false questions.
-   **Data Cleaning:** The text from the API sometimes included HTML entities (e.g., `&quot;` instead of `"`). I used Python's built-in `html` library and its `html.unescape()` method to clean the question text before displaying it.

```python
# In data.py
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("[https://opentdb.com/api.php](https://opentdb.com/api.php)", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
```

---

### 3. Structuring the UI with a Class
To keep the code organized and maintain a good separation of concerns, the entire user interface was encapsulated within its own class, `QuizInterface`.

-   **The `__init__` Method:** This method is responsible for creating the main window, the score label, the question canvas, and the true/false buttons. All UI setup happens here.
-   **Connecting Logic and UI:** The `QuizBrain` object (which handles the game logic) is passed into the `QuizInterface` during initialization. This allows the UI to communicate with the game logic. For example, when a button is clicked, the UI can call a method like `self.quiz.check_answer()`. This is a much cleaner approach than mixing UI and logic code in the same file.

---

### 4. Type Hinting and Code Safety
I made the code more robust and easier to understand by adding type hints. This is especially useful in an OOP context where objects are passed between different classes.

-   **Specifying Object Types:** By hinting the type of the `quiz_brain` parameter in the `QuizInterface`'s `__init__` method, my IDE (PyCharm) could provide better auto-completion and static error checking.
-   **Example:** `def __init__(self, quiz_brain: QuizBrain):` clearly states that this method expects an object of the `QuizBrain` class. If I were to pass in a list or a string by mistake, the IDE would warn me immediately.

---

### 5. Providing Instant User Feedback
A good GUI gives the user immediate feedback on their actions.

-   **Flashing the Canvas:** When the user clicks an answer button, the `give_feedback()` method is called. This method checks if the answer was correct and changes the canvas background color to green for correct or red for incorrect.
-   **Timed Delay with `window.after()`:** The color flash is temporary. I used `window.after(1000, self.get_next_question)` to schedule the `get_next_question` method to run after a 1-second (1000 ms) delay. This function fetches the next question and, importantly, resets the canvas background color back to white, preparing the UI for the next round.

---

### 6. Final Project Code
The project is split into multiple files to separate concerns, a key principle of good software design.

```python
# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
```

```python
# ui.py
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
```

```python
# quiz_brain.py
import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
```

```python
# data.py
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("[https://opentdb.com/api.php](https://opentdb.com/api.php)", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
```

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```