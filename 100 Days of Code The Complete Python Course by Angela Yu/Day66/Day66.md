# Day 66: Building a RESTful API with Flask

Welcome to Day 66! Today, we shifted from building traditional websites to creating a powerful backend service: a RESTful API. The goal was to take our "Cafe & Wifi" database and expose it to the world, allowing other applications to programmatically access and manipulate our data.

Instead of rendering HTML templates, our Flask application now serves data in a standardized JSON format. This project is the foundation of many modern web services and demonstrates how to build a robust, data-centric backend.



## Table of Contents
- [1. What is a REST API?](#1-what-is-a-rest-api)
- [2. Building the API Endpoints](#2-building-the-api-endpoints)
- [3. Implementing CRUD with HTTP Methods](#3-implementing-crud-with-http-methods)
- [4. Handling Requests and Sending JSON Responses](#4-handling-requests-and-sending-json-responses)
- [5. API Authentication and Documentation](#5-api-authentication-and-documentation)
- [6. Day 66 Project: Cafe & Wifi API Code](#6-day-66-project-cafe--wifi-api-code)

---

### 1. What is a REST API?
A REST (Representational State Transfer) API is an architectural style for designing networked applications. It's not a specific technology but a set of principles that makes communication between a client (like a mobile app or another server) and our server predictable and stateless.

Key principles include:
-   **Client-Server Architecture:** The UI is separate from the data storage.
-   **Statelessness:** Each request from a client contains all the information needed to process it. The server doesn't store any client state between requests.
-   **Uniform Interface:** Using standard HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) to interact with resources (our cafes).

---

### 2. Building the API Endpoints
Each "endpoint" is a specific URL that performs a particular action. For our Cafe API, we created several endpoints to handle different operations:

-   `/random`: Get a random cafe from the database.
-   `/all`: Get all cafes.
-   `/search`: Find a cafe by its location.
-   `/add`: Add a new cafe to the database.
-   `/update-price/<cafe_id>`: Update the coffee price of a specific cafe.
-   `/report-closed/<cafe_id>`: Delete a cafe from the database.

---

### 3. Implementing CRUD with HTTP Methods
We mapped the four CRUD operations to the standard HTTP methods, which is a core concept of REST design:

-   **Create (POST):** The `/add` endpoint listens for `POST` requests. It receives new cafe data in the request body, creates a new `Cafe` object, and adds it to the database.
-   **Read (GET):** The `/all`, `/random`, and `/search` endpoints use `GET` requests to retrieve data without modifying it.
-   **Update (PATCH):** The `/update-price` endpoint uses a `PATCH` request. `PATCH` is used for making partial modifications to a resource (in this case, just changing the price).
-   **Delete (DELETE):** The `/report-closed` endpoint uses a `DELETE` request to remove a specific cafe record from the database.

---

### 4. Handling Requests and Sending JSON Responses
The biggest change from previous projects was how we handled data.

-   **`request.args` and `request.form`:** We used `request.args` to get data from URL query parameters (e.g., `?loc=Peckham`) and `request.form` to get data from a submitted form body (for `POST` requests).
-   **`jsonify`:** Instead of `render_template`, we used Flask's `jsonify` function. This function serializes our Python dictionaries and SQLAlchemy objects into a proper JSON format and sets the correct `Content-Type` header (`application/json`), which is what API clients expect.
-   **Error Handling:** We returned meaningful JSON error messages with appropriate HTTP status codes (e.g., `404 Not Found`, `403 Forbidden`) to help the API consumer understand what went wrong.

---

### 5. API Authentication and Documentation
-   **Authentication:** To protect sensitive endpoints like our `DELETE` route, we implemented a simple API key authentication. The client must provide a valid `api-key` as a query parameter, which the server checks before proceeding.
-   **Documentation:** An API is useless if no one knows how to use it. We used **Postman**, a popular API client, to test our endpoints and then used its features to automatically generate and publish professional documentation for our API.

---

### 6. Day 66 Project: Cafe & Wifi API Code
Here is the final `main.py` code, which acts as a standalone REST API server.

```python
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# --- Database Setup ---
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# --- Cafe Table Configuration ---
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

# --- API Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
```