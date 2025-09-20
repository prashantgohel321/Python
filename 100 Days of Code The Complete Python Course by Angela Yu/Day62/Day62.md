# Day 62: Coffee & Wifi Website

Welcome to Day 62! This was a capstone project that brought together all the web development skills we've learned so far. We built a data-driven website called "Coffee & Wifi" that helps users find cafes that are good for working. The application reads data from a CSV file, displays it in a table, and allows users to contribute by adding new cafes through a web form.

This project was a practical application of Flask, WTForms, Bootstrap, and data handling with Python's built-in `csv` module.



## Table of Contents
- [1. Project Goal: A Crowdsourced Cafe Directory](#1-project-goal-a-crowdsourced-cafe-directory)
- [2. The Form: Creating `CafeForm` with WTForms](#2-the-form-creating-cafeform-with-wtforms)
- [3. The Routes: Serving Pages and Handling Data](#3-the-routes-serving-pages-and-handling-data)
- [4. The Templates: Displaying and Adding Data](#4-the-templates-displaying-and-adding-data)
- [5. Day 62 Project: Coffee & Wifi Code](#5-day-62-project-coffee--wifi-code)

---

### 1. Project Goal: A Crowdsourced Cafe Directory
The main objective was to create a web application that:
1.  Displays a list of cafes from a pre-existing `cafe-data.csv` file.
2.  Provides a form for users to add new cafes to the list.
3.  Appends the user-submitted data to the `cafe-data.csv` file.
4.  Uses Bootstrap for a clean and responsive layout.

---

### 2. The Form: Creating `CafeForm` with WTForms
The core of the data submission functionality is the `CafeForm` class, built using Flask-WTF. This form defines all the fields needed to add a new cafe.

-   **Fields:** We used various field types to capture the right data:
    -   `StringField` for text inputs like the cafe name, location URL, and opening/closing times.
    -   `SelectField` for fields with a predefined set of choices, like the ratings for coffee, wifi, and power. This provides a user-friendly dropdown menu.
-   **Validators:** We used validators to ensure data quality:
    -   `DataRequired()` was used on all fields to make them mandatory.
    -   `URL()` was used on the location field to ensure the user provides a valid URL.

```python
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')
```

---

### 3. The Routes: Serving Pages and Handling Data
We defined three main routes in `main.py`:

-   **`@app.route('/')` (Home):** Renders the `index.html` homepage.
-   **`@app.route('/cafes')` (Cafes):** This is where the data reading happens. The function opens `cafe-data.csv`, reads its contents line by line using the `csv` module, and converts it into a list of lists. This list is then passed to the `cafes.html` template to be rendered.
-   **`@app.route('/add', methods=["GET", "POST"])` (Add Cafe):** This route handles both displaying the form and processing the submission.
    -   On a `GET` request, it simply renders the `add.html` page with an empty `CafeForm`.
    -   On a `POST` request (when the form is submitted), `form.validate_on_submit()` checks the data. If valid, the function opens `cafe-data.csv` in **append mode** (`mode="a"`) and writes the new data as a comma-separated line. Finally, it redirects the user to the `/cafes` page to see their new entry.

---

### 4. The Templates: Displaying and Adding Data
-   **`cafes.html`:** This template receives the list of all cafes from the server. It uses a nested Jinja `for` loop to iterate through each row and each item in the row, building an HTML `<table>`. An `if` statement checks if an item is a URL to render it as a clickable "Maps Link".
-   **`add.html`:** This template uses the `render_form(form)` macro from Bootstrap-Flask to display the `CafeForm`. We set `novalidate=True` in the `render_form` call to disable default browser validation, allowing our WTForms validators to handle everything.

---

### 5. Day 62 Project: Coffee & Wifi Code
Here is the final `main.py` code that powers the application.

**`main.py`:**
```python
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
```