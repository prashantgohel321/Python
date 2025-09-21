# Day 64: My Top 10 Movies Website

Welcome to Day 64! This project combines our knowledge of databases with external APIs to build a dynamic "Top 10 Movies" website. It's a full-stack Flask application where users can create a personalized, ranked list of their favorite films.

The application allows a user to search for a movie, add it to their personal database, and then rate and review it. The homepage then displays all the added movies, automatically ranking them from highest to lowest rating. This project is a fantastic example of integrating a local database with a third-party data source to create a rich user experience.

## Table of Contents
- [1. Project Goal: A Dynamic Movie Ranking Site](#1-project-goal-a-dynamic-movie-ranking-site)
- [2. Database Model and API Integration](#2-database-model-and-api-integration)
- [3. The "Add Movie" Flow (Create)](#3-the-add-movie-flow-create)
- [4. Editing and Deleting Movies (Update & Delete)](#4-editing-and-deleting-movies-update--delete)
- [5. The Dynamic Ranking Logic](#5-the-dynamic-ranking-logic)
- [6. Day 64 Project: Top Movies Website Code](#6-day-64-project-top-movies-website-code)

---

### 1. Project Goal: A Dynamic Movie Ranking Site
The objective was to create a web app that could:
1.  Display a list of movies from a local SQLite database.
2.  Allow users to add new movies by searching the The Movie Database (TMDB) API.
3.  Allow users to edit the rating and review of each movie.
4.  Allow users to delete movies from their list.
5.  Automatically rank the movies on the homepage based on their user-assigned rating.

---

### 2. Database Model and API Integration
The foundation of the project is the `Movie` database model and the connection to the TMDB API.

-   **SQLAlchemy Model:** We defined a `Movie` table with columns to store all the necessary information, including `rating`, `ranking`, `review`, and data fetched from the API like `title`, `year`, `description`, and `img_url`.
    ```python
    class Movie(db.Model):
        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
        year: Mapped[int] = mapped_column(Integer, nullable=False)
        description: Mapped[str] = mapped_column(String(500), nullable=False)
        rating: Mapped[float] = mapped_column(Float, nullable=True)
        ranking: Mapped[int] = mapped_column(Integer, nullable=True)
        review: Mapped[str] = mapped_column(String(250), nullable=True)
        img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    ```
-   **TMDB API:** We used the `requests` library to interact with the TMDB API. An API key is required. We used two main endpoints: one for searching for movies by title and another for fetching detailed information about a specific movie using its ID.

---

### 3. The "Add Movie" Flow (Create)
Adding a movie is a two-step process that bridges our app and the TMDB API:
1.  **Search:** The `/add` route presents a simple WTForm (`FindMovieForm`). When the user submits a movie title, the app sends a request to the TMDB search API.
2.  **Select:** The search results (a list of potential movies) are passed to a `select.html` template. The user then clicks on the correct movie from the list.
3.  **Fetch & Add:** Clicking a movie triggers the `/find` route, passing the movie's TMDB ID. This route then fetches the detailed movie data from the TMDB info endpoint, creates a new `Movie` object with that data, saves it to our local database, and redirects the user to the `/edit` page to set an initial rating and review.

---

### 4. Editing and Deleting Movies (Update & Delete)
-   **Update:** The `/edit` route allows users to update a movie's rating and review. It uses a `RateMovieForm` (a WTForm). When submitted, it finds the movie in our database by its `id`, updates the `rating` and `review` fields, and commits the changes.
-   **Delete:** The `/delete` route finds a movie by its `id` and uses `db.session.delete()` to remove it from the database, then redirects back to the homepage.

---

### 5. The Dynamic Ranking Logic
This is the cleverest part of the application. Instead of storing a fixed rank, we calculate it every time the homepage is loaded.
1.  **Query and Order:** In the home (`/`) route, we query the database for all movies but use `.order_by(Movie.rating)` to fetch them sorted by their rating in ascending order.
2.  **Assign Rank:** We then iterate through this sorted list of movies. With a simple counter, we assign a `ranking` to each movie object based on its position in the sorted list. The highest-rated movie gets the #1 rank, the second-highest gets #2, and so on.
3.  **Render:** This newly ranked list of movie objects is then passed to `index.html` to be displayed. This ensures the ranking is always up-to-date after any rating is edited.

---

### 6. Day 64 Project: Top Movies Website Code
Here is the final `main.py` code, showcasing the integration of the database, API, and forms.

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# --- TMDB API Configuration ---
MOVIE_DB_API_KEY = "YOUR_TMDB_API_KEY"  # Replace with your key
MOVIE_DB_SEARCH_URL = "[https://api.themoviedb.org/3/search/movie](https://api.themoviedb.org/3/search/movie)"
MOVIE_DB_INFO_URL = "[https://api.themoviedb.org/3/movie](https://api.themoviedb.org/3/movie)"
MOVIE_DB_IMAGE_URL = "[https://image.tmdb.org/t/p/w500](https://image.tmdb.org/t/p/w500)"

# --- Flask App Setup ---
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# --- Database Setup ---
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# --- Database Model ---
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

# --- WTForms ---
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# --- Flask Routes ---
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
```