# Day 63: Virtual Bookshelf with SQLite and SQLAlchemy

Welcome to Day 63! Today we took a significant leap by replacing our simple file-based data storage (like CSVs) with a robust and persistent database. We built a "Virtual Bookshelf" application where users can track the books they've read and manage their ratings.

This project was a deep dive into databases using **SQLite** and the powerful **Flask-SQLAlchemy** extension. We learned how to set up a database, define data structures (models), and perform the four fundamental database operations: Create, Read, Update, and Delete (CRUD).



## Table of Contents
- [1. From CSV to a Real Database](#1-from-csv-to-a-real-database)
- [2. Setting Up the Database with Flask-SQLAlchemy](#2-setting-up-the-database-with-flask-sqlalchemy)
- [3. CRUD Operations: The Core of the Application](#3-crud-operations-the-core-of-the-application)
- [4. Day 63 Project: Virtual Bookshelf Code](#4-day-63-project-virtual-bookshelf-code)

---

### 1. From CSV to a Real Database
While CSV files are useful, they are not ideal for complex applications. Databases offer many advantages:
-   **Data Integrity:** They can enforce data types and rules.
-   **Scalability:** They handle large amounts of data efficiently.
-   **Relationships:** They allow us to define complex relationships between different types of data.
-   **Structured Queries:** They provide a powerful language (SQL) for retrieving and manipulating data.

For this project, we used **SQLite**, a self-contained, serverless database engine that is perfect for learning and small to medium-sized applications.

---

### 2. Setting Up the Database with Flask-SQLAlchemy
Flask-SQLAlchemy is an extension that simplifies using SQLAlchemy (a Python SQL toolkit) with Flask. It helps us interact with our database using Python objects instead of raw SQL queries.

The setup involved several key steps:
1.  **Configuration:** We configured our Flask app to connect to our SQLite database file (`books.db`).
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
    ```
2.  **Initialization:** We created a `db` object by initializing `SQLAlchemy` with our app.
3.  **Defining a Model:** We created a `Book` class that inherits from `db.Model`. This class defines the structure of our `books` table in the database. Each attribute of the class represents a column in the table. We used `Mapped` and `mapped_column` to define columns with specific types (`Integer`, `String`, `Float`) and constraints (`primary_key=True`, `unique=True`, `nullable=False`).
    ```python
    class Book(db.Model):
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
        author: Mapped[str] = mapped_column(String(250), nullable=False)
        rating: Mapped[float] = mapped_column(Float, nullable=False)
    ```
4.  **Creating the Table:** Finally, we used `db.create_all()` within an application context (`with app.app_context():`) to create the database file and the `book` table based on our model.

---

### 3. CRUD Operations: The Core of the Application
The bulk of the project was implementing the four CRUD operations, each tied to a specific Flask route.

-   **Create:** The `/add` route handles adding new books. When the form is submitted (`POST` request), it creates a new `Book` object with the data from the form, adds it to the database session with `db.session.add(new_book)`, and saves it permanently with `db.session.commit()`.

-   **Read:**
    -   To read *all* books, the home route (`/`) queries the database using `db.session.execute(db.select(Book).order_by(Book.title))`. The result is a list of `Book` objects that is passed to the `index.html` template to be displayed.
    -   To read a *single* book (for editing), we use `db.get_or_404(Book, book_id)` which fetches a book by its primary key or returns a 404 Not Found error if it doesn't exist.

-   **Update:** The `/edit` route allows users to change a book's rating. On a `POST` request, it finds the specific book by its ID, updates its `rating` attribute with the new value from the form, and commits the change to the database with `db.session.commit()`.

-   **Delete:** The `/delete` route removes a book from the library. It gets the book's ID from the URL, retrieves the corresponding `Book` object, and removes it using `db.session.delete(book_to_delete)` followed by `db.session.commit()`.

---

### 4. Day 63 Project: Virtual Bookshelf Code
Here is the complete `main.py` file, demonstrating the full implementation of the database and all the CRUD routes.

**`main.py`:**
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # READ ALL RECORDS
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
```