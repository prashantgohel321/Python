# Day 68: Authentication with Flask-Login

Welcome to Day 68! Today's focus was on building a secure authentication system from scratch. I learned how to create user accounts, manage login sessions, and protect content so that it's only accessible to authenticated users.

This is a fundamental skill for any web developer, as it's the basis for creating personalized user experiences and securing sensitive data. I used Flask-Login and Werkzeug's security helpers to achieve this.

## Table of Contents
- [1. User Registration and Database Setup](#1-user-registration-and-database-setup)
- [2. Password Security: Hashing and Salting](#2-password-security-hashing-and-salting)
- [3. Implementing Login with Flask-Login](#3-implementing-login-with-flask-login)
- [4. Protecting Routes](#4-protecting-routes)
- [5. Providing User Feedback with Flash Messages](#5-providing-user-feedback-with-flash-messages)
- [6. Day 68 Project: Final Code](#6-day-68-project-final-code)

---

### 1. User Registration and Database Setup
The first step was to allow new users to register. This involved:
-   **Creating a User Model:** I set up a `User` table in my SQLite database using SQLAlchemy. A critical addition to this model was inheriting from `UserMixin`, a class provided by Flask-Login that includes default implementations for properties like `is_authenticated`.
-   **Handling Form Submission:** The `/register` route accepts `POST` requests from the registration form. It takes the user's name, email, and password to create a new `User` object.

---

### 2. Password Security: Hashing and Salting
Storing passwords in plaintext is a massive security vulnerability. To fix this, I implemented hashing and salting.

-   **What is Hashing?** Hashing is a one-way process that turns a password into a long, fixed-size string of characters. It's designed to be irreversible, meaning you can't get the original password back from the hash.
-   **What is Salting?** To prevent attackers from using pre-computed "rainbow tables" to crack common passwords, I added a "salt" — a random string of characters — to each password before hashing it. This ensures that even identical passwords will have unique hashes in the database.
-   **Implementation:** I used the `generate_password_hash` function from `werkzeug.security`. This function handles both hashing and salting in one step. The resulting hash is what gets stored in the database, not the original password.

```python
from werkzeug.security import generate_password_hash

# Hashing and salting the password entered by the user
hash_and_salted_password = generate_password_hash(
    request.form.get('password'),
    method='pbkdf2:sha256',
    salt_length=8
)
# Storing the hashed password in our database
new_user = User(
    email=request.form.get('email'),
    name=request.form.get('name'),
    password=hash_and_salted_password,
)
db.session.add(new_user)
db.session.commit()
```

---

### 3. Implementing Login with Flask-Login
Flask-Login simplifies the process of managing user sessions. Here’s how I set it up:
-   **Initialization:** I created a `LoginManager` instance and linked it to my Flask app.
-   **User Loader:** I implemented a `user_loader` function. This function is used by Flask-Login to retrieve a user object from the database based on their user ID, which is stored in the session cookie.
-   **Login Route:** The `/login` route finds the user by their email. It then uses `werkzeug.security.check_password_hash()` to compare the password the user entered with the hashed password stored in the database. If they match, `login_user(user)` is called to create a session for that user.

---

### 4. Protecting Routes
With login functionality in place, I could now restrict access to certain pages.
-   **`@login_required` Decorator:** By adding this decorator to routes like `/secrets` and `/download`, Flask-Login will automatically prevent unauthenticated users from accessing them. If a logged-out user tries to visit these pages, they will be redirected to the login page.
-   **`current_user`:** Flask-Login provides a `current_user` proxy object, which represents the currently logged-in user. This allowed me to access their properties (like `current_user.name`) in my templates and routes, and check their status with `current_user.is_authenticated`.

---

### 5. Providing User Feedback with Flash Messages
To improve the user experience, I used Flask's flash messaging system to provide feedback.
-   **Flashing a Message:** In the `/login` and `/register` routes, I used the `flash()` function to create a one-time message if something went wrong (e.g., "Password incorrect" or "You've already signed up").
-   **Rendering Messages:** In the template (`login.html`), I used a `with get_flashed_messages()` block to check for and display any flashed messages. These messages are cleared from the session after they are displayed once.

---

### 6. Day 68 Project: Final Code
Here is the complete `main.py` for the authentication project, bringing all these concepts together.

```python
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB with the UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name'),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
```