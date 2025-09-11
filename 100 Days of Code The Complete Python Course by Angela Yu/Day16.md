# Day 16: An Introduction to Object-Oriented Programming (OOP)

Welcome to my log for Day 16! Today marked a fundamental shift in how I think about and structure my code. I moved from procedural programming (writing code as a series of steps) to **Object-Oriented Programming (OOP)**. This paradigm is all about modeling real-world concepts as objects, which helps to manage complexity and create more reusable and organized code. The project for the day was to take the coffee machine from Day 15 and rebuild it using OOP principles.

## Table of Contents
- [1. What is Object-Oriented Programming (OOP)?](#1-what-is-object-oriented-programming-oop)
- [2. Classes and Objects: Blueprints and Instances](#2-classes-and-objects-blueprints-and-instances)
- [3. Working with Objects: Attributes and Methods](#3-working-with-objects-attributes-and-methods)
- [4. Using External Packages: PyPI and `prettytable`](#4-using-external-packages-pypi-and-prettytable)
- [5. Day 16 Project: The Coffee Machine, OOP Edition](#5-day-16-project-the-coffee-machine-oop-edition)
- [6. Final Project Code](#6-final-project-code)

---

### 1. What is Object-Oriented Programming (OOP)?
Procedural programming, which I've been doing so far, involves writing procedures (or functions) that perform operations on data. As programs like the coffee machine get more complex, the web of functions and variables can become tangled and hard to manage, like spaghetti code.

OOP offers a better way to structure code for complex projects. It works by modeling real-world things as self-contained **objects**. Think of running a restaurant:
-   **Procedural Approach:** One person (you) does everything—takes orders, cooks, cleans, etc. It's chaotic and doesn't scale.
-   **OOP Approach:** You hire specialized staff—a chef, a waiter, a cleaner. Each person (object) knows their job. You, the manager, just need to tell the waiter to take an order; you don't need to know the specifics of *how* they do it.

This approach makes code more modular, easier to manage, and reusable.

---

### 2. Classes and Objects: Blueprints and Instances
In OOP, we model these real-world things using **classes** and **objects**.

-   **Class:** A blueprint for creating an object. It defines the properties and behaviors that all objects of a certain type will have. For example, a `Car` class would define that all cars have wheels and can drive. -   **Object:** An actual instance created from a class. While the `Car` class is the blueprint, a specific `my_tesla` variable would be an object—a tangible car created from that blueprint, with its own specific color and mileage.

An object has two key components:
-   **Attributes:** What the object *has*. These are variables that belong to the object and store its state (e.g., `is_holding_plate`, `tables_responsible`).
-   **Methods:** What the object *does*. These are functions that belong to the object and define its behavior (e.g., `take_order()`, `take_payment()`).

---

### 3. Working with Objects: Attributes and Methods
I practiced creating and working with objects using Python's built-in `turtle` graphics library.

-   **Creating an Object:** To create an object, I call the class like a function.
    ```python
    from turtle import Turtle, Screen
    
    # Create a new object 'timmy' from the 'Turtle' class
    timmy = Turtle() 
    # Create a new object 'my_screen' from the 'Screen' class
    my_screen = Screen()
    ```

-   **Accessing Attributes:** I can get or set an object's attributes using dot notation.
    ```python
    # Get the value of the canvheight attribute
    print(my_screen.canvheight) 
    ```

-   **Calling Methods:** I can make an object perform an action by calling its methods, also using dot notation.
    ```python
    # Call the forward() method on the timmy object
    timmy.forward(100) 
    # Call the exitonclick() method on the my_screen object
    my_screen.exitonclick()
    ```

---

### 4. Using External Packages: PyPI and `prettytable`
Python has a vast ecosystem of third-party libraries that I can install and use.
-   **PyPI (Python Package Index):** The official repository for Python packages.
-   **Installing a Package:** In PyCharm, I learned to install packages by going to `Preferences -> Project: [ProjectName] -> Python Interpreter` and clicking the `+` button to search for and install packages like `prettytable`.
-   **Using an Installed Package:** Once installed, I can import classes from it just like any other module and create objects to use in my code.

```python
from prettytable import PrettyTable

# Create an object from the PrettyTable class
table = PrettyTable()

# Call methods on the object
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change an attribute
table.align = "l"

print(table)
```

---

### 5. Day 16 Project: The Coffee Machine, OOP Edition
The main project was to rewrite the Day 15 Coffee Machine using OOP. I was given pre-written classes (`CoffeeMaker`, `MoneyMachine`, `Menu`, `MenuItem`) and my task was to use them to build the application. I didn't have to worry about the *implementation* of the classes, only how to *use* them based on their documentation.

My main `main.py` file became much simpler and more readable. It acted as the "manager," creating objects and calling their methods to get the job done.

1.  **Create Objects:** I started by creating instances of `CoffeeMaker`, `MoneyMachine`, and `Menu`.
2.  **Main Loop:** The logic was placed inside a `while` loop.
3.  **Delegate Tasks:** Instead of writing complex logic myself, I delegated tasks to the objects:
    -   Get the list of drinks from the `Menu` object.
    -   Find the specific drink using a method on the `Menu` object.
    -   Check if resources are sufficient using a method on the `CoffeeMaker` object.
    -   Process payment using a method on the `MoneyMachine` object.
    -   Make the coffee using a method on the `CoffeeMaker` object.

This approach made the code much cleaner and easier to understand, as each object was responsible for its own area of expertise.

---

### 6. Final Project Code
Here is the complete code for the OOP version of the Coffee Machine. My work was entirely in `main.py`; the other files were provided as the "library" I was using.

```python
# main.py
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

```

```python
# menu.py
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a concatenated string."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip("/")

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
```

```python
# coffee_maker.py
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
```

```python
# money_machine.py
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
```