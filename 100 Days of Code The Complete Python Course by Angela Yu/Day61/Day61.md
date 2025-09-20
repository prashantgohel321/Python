# Day 61: Building Advanced Forms with Flask-WTF

Welcome to Day 61! Today's focus was on leveling up our web forms by using **Flask-WTF**, a Flask extension that integrates with the WTForms library. This allows for more robust, secure, and maintainable forms compared to writing raw HTML. We built a "Secrets" website with a login page that validates user input before granting access.

The project also introduced two other crucial concepts for building scalable web applications: **Bootstrap-Flask** for easy styling and **Jinja Template Inheritance** for keeping our HTML code DRY (Don't Repeat Yourself).


## Table of Contents
- [1. Why Use Flask-WTF?](#1-why-use-flask-wtf)
- [2. Creating a Form with a Python Class](#2-creating-a-form-with-a-python-class)
- [3. Jinja Template Inheritance](#3-jinja-template-inheritance)
- [4. Rendering the Form with Bootstrap-Flask](#4-rendering-the-form-with-bootstrap-flask)
- [5. Validation and Handling Form Data](#5-validation-and-handling-form-data)
- [6. Day 61 Project: Secrets Website Code](#6-day-61-project-secrets-website-code)

---

### 1. Why Use Flask-WTF?
While standard HTML forms work, Flask-WTF offers significant advantages:
-   **Easy Validation:** It comes with built-in validators to check if data is in the correct format (e.g., a valid email address) or meets certain criteria (e.g., minimum password length).
-   **Less Code:** It reduces the amount of repetitive HTML you need to write for forms.
-   **CSRF Protection:** It automatically includes a hidden CSRF (Cross-Site Request Forgery) token in every form, a crucial security feature that helps prevent malicious attacks.

---

### 2. Creating a Form with a Python Class
With Flask-WTF, forms are defined in Python as classes that inherit from `FlaskForm`. Each form field is an instance of a WTForms field class (`StringField`, `PasswordField`, etc.).

Validators are passed as a list to the `validators` argument of each field. For this to work, the Flask application needs a `secret_key` to be configured, which is used to generate the secure CSRF token.

**Form Definition in `main.py`:**
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

# In the main app setup
app = Flask(__name__)
app.secret_key = "a-very-secret-key"
```

---

### 3. Jinja Template Inheritance
To avoid repeating the same HTML boilerplate (like `<html>`, `<head>`, `<body>`, and Bootstrap links) on every page, we used Jinja's template inheritance.

1.  **`base.html`:** We created a parent template with the basic HTML structure. It contains `{% block %}` tags that act as placeholders for content (`{% block content %}`) and the title (`{% block title %}`).
2.  **Child Templates:** Other pages like `login.html` and `index.html` *extend* this base template using `{% extends "base.html" %}`. They then fill in the defined blocks with their own specific content.

This makes the site much easier to manage. For example, to add a new CSS file to the entire site, you only need to change `base.html`.

---

### 4. Rendering the Form with Bootstrap-Flask
The **Bootstrap-Flask** extension makes styling our WTForm incredibly simple. After initializing it in `main.py`, we can render a fully-styled Bootstrap form with a single line of code in our template.

1.  **Import the Macro:** In `login.html`, we import the `render_form` macro: `{% from 'bootstrap5/form.html' import render_form %}`.
2.  **Render the Form:** We then call this macro, passing in the form object that we sent from our Flask route: `{{ render_form(form) }}`.

This one line generates all the necessary HTML for labels, inputs, error messages, and the submit button, all with the correct Bootstrap classes.

---

### 5. Validation and Handling Form Data
In our `/login` route, we handle both displaying the form (`GET` request) and processing it (`POST` request).

-   We create an instance of our `LoginForm`.
-   `form.validate_on_submit()` is a powerful method that checks two things: if the request is a `POST` request and if the data passes all the validators we defined in the `LoginForm` class.
-   If validation is successful, we can access the submitted data securely using `form.<field_name>.data`.
-   We then check if the email and password match our predefined admin credentials and render either a `success.html` or `denied.html` page accordingly.
-   If it's a `GET` request or if validation fails, we just render the `login.html` template, passing the `form` object to it. WTForms and Bootstrap-Flask will automatically display any validation errors next to the relevant fields.

---

### 6. Day 61 Project: Secrets Website Code
Here is the final `main.py` that brings all these concepts together.

**`main.py`:**
```python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

# Define the login form class
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters.")])
    submit = SubmitField(label="Log In")

# Initialize Flask App
app = Flask(__name__)
app.secret_key = "a-long-and-very-secret-string-for-csrf"

# Initialize Bootstrap-Flask
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # This block runs only on POST request after data is submitted
    if login_form.validate_on_submit():
        # Check credentials
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # This runs on GET request or if validation fails
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
```