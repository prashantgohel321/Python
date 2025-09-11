# Day 17: Creating My Own Classes

Welcome to my log for Day 17! Today, I transitioned from being a *user* of classes to a *creator* of classes. The focus was on learning the syntax and structure for building my own custom blueprints in Python. This is a huge step in Object-Oriented Programming, as it unlocks the ability to model any concept I can imagine. I applied this new skill to build a fully functional quiz game, architected entirely with classes I designed myself.

## Table of Contents
- [1. How to Create a Class in Python](#1-how-to-create-a-class-in-python)
  - [The `class` Keyword and PascalCase Naming](#the-class-keyword-and-pascalcase-naming)
  - [The Constructor: The `__init__()` Method](#the-constructor-the-__init__-method)
  - [Adding Attributes to a Class](#adding-attributes-to-a-class)
  - [Adding Methods to a Class](#adding-methods-to-a-class)
- [2. Day 17 Project: The Quiz Game](#2-day-17-project-the-quiz-game)
  - [Breaking Down the Problem into Objects](#breaking-down-the-problem-into-objects)
  - [The `Question` Class](#the-question-class)
  - [The `QuizBrain` Class](#the-quizbrain-class)
- [3. Final Project Code](#3-final-project-code)

---

### 1. How to Create a Class in Python
Creating a class is like designing a blueprint. It defines what objects created from it will look like and what they will be able to do.

#### The `class` Keyword and PascalCase Naming
I start by using the `class` keyword. By convention, class names in Python are written in **PascalCase**, where the first letter of each word is capitalized (e.g., `MyAwesomeClass`). This helps distinguish classes from variables and functions, which typically use `snake_case`.

```python
class User:
    pass # 'pass' is used here as a placeholder for an empty class
```

#### The Constructor: The `__init__()` Method
The constructor is a special method that gets called every time a new object is created from the class. It's where I set up the initial state of the object. In Python, the constructor is named `__init__()`.

-   It's a function defined inside the class.
-   The `self` parameter is mandatory as the first argument. It refers to the specific object instance that is being created.

#### Adding Attributes to a Class
Attributes are the variables that belong to an object. I define them within the `__init__` method to ensure every object created from the class has them.

-   **Attributes from Parameters:** I can pass arguments when creating an object, and these can be used to set the initial values of attributes.
-   **Default Attributes:** I can also set attributes to a default value directly within the `__init__` method, without needing a parameter.

```python
class User:
    def __init__(self, user_id, username):
        # Attributes set from parameters
        self.id = user_id
        self.username = username
        # Attribute with a default value
        self.followers = 0
```
Now, when I create a `User` object, I must provide the `user_id` and `username`.
```python
user_1 = User("001", "angela")
# user_1.id is "001"
# user_1.username is "angela"
# user_1.followers is 0
```

#### Adding Methods to a Class
Methods are functions that belong to a class and define what an object can do. They are defined just like regular functions but are placed inside the class indentation.

-   The first parameter of any method must always be `self`. This allows the method to access and modify the object's attributes.

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
```
In this example, the `follow` method takes `self` (the user doing the following) and `user` (the user being followed) as arguments and modifies their attributes accordingly.

---

### 2. Day 17 Project: The Quiz Game
The project was to build a command-line quiz game. I had to create the entire structure using OOP.

#### Breaking Down the Problem into Objects
I first analyzed the game's requirements and identified two distinct concepts that could be modeled as objects:

1.  **A Question:** An individual question has two key pieces of data: its text and its correct answer.
2.  **The Quiz Brain:** This is the engine of the game. It needs to manage the list of questions, keep track of the current question number, check the user's answer, and track the score.

#### The `Question` Class
I created `question_model.py` to hold this class. Its job is simple: to model a single question.
-   **Attributes:** `text` and `answer`.
-   **Constructor (`__init__`):** Takes the question text and answer as input and saves them as attributes.

#### The `QuizBrain` Class
I created `quiz_brain.py` for the main game logic.
-   **Attributes:**
    -   `question_number`: Starts at 0 and increments with each question.
    -   `score`: Starts at 0 and increments with each correct answer.
    -   `question_list`: A list of `Question` objects passed in during initialization.
-   **Methods:**
    -   `still_has_questions()`: Returns `True` if the current `question_number` is less than the total number of questions, `False` otherwise. This method controls the main game loop.
    -   `next_question()`: Fetches the current question from the `question_list`, prompts the user with the question text, and gets their input.
    -   `check_answer()`: Compares the user's answer to the correct answer for the current question. It provides feedback and updates the score if they are correct.

The `main.py` file became very clean. Its only jobs were to create the list of `Question` objects from the data, create a `QuizBrain` object, and run the main game loop.

---

### 3. Final Project Code
Here is the complete code for the Quiz Game, split into its three main files.

```python
# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

```

```python
# question_model.py
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

```python
# quiz_brain.py
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

```

```python
# data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    # ... more questions
]
```