# Day 15: The Coffee Machine Project

Welcome to my log for Day 15! Today's project was a practical and comprehensive challenge: building a virtual coffee machine.  This wasn't just about a single game loop; it involved managing state, handling different types of user input, and making sure all the different parts of the program worked together seamlessly. I had to think like a software developer, breaking down the machine's requirements into functions and logical steps to create a working product.

## Table of Contents
- [1. Project Requirements](#1-project-requirements)
- [2. Program Features I Implemented](#2-program-features-i-implemented)
  - [Feature 1: Print a Report](#feature-1-print-a-report)
  - [Feature 2: Check Resource Sufficiency](#feature-2-check-resource-sufficiency)
  - [Feature 3: Process Coins](#feature-3-process-coins)
  - [Feature 4: Check Transaction Success](#feature-4-check-transaction-success)
  - [Feature 5: Make Coffee & Deduct Resources](#feature-5-make-coffee--deduct-resources)
- [3. My Approach and Code Structure](#3-my-approach-and-code-structure)
- [4. Final Project Code: The Coffee Machine](#4-final-project-code-the-coffee-machine)

---

### 1. Project Requirements
The coffee machine needed to perform several key actions based on user input:

1.  **Serve three types of coffee:** Espresso, Latte, and Cappuccino, each with its own recipe and cost.
2.  **Manage resources:** Keep track of the internal supply of water, milk, and coffee.
3.  **Process payments:** Accept four types of US coins (quarters, dimes, nickels, pennies) and calculate the total value.
4.  **Check transactions:** Ensure the user has inserted enough money for the selected drink and provide change if necessary.
5.  **Provide reports:** Display the current resource levels when the user types "report".
6.  **Turn off:** Allow a "maintainer" to shut down the machine using the "off" command.

---

### 2. Program Features I Implemented

#### Feature 1: Print a Report
-   **What:** When the user enters "report", the program should display the current amounts of water, milk, coffee, and money inside the machine.
-   **How:** I used an `elif choice == "report":` block to catch this command. Inside, I printed f-strings that accessed the values from my `resources` dictionary and the `profit` variable.

#### Feature 2: Check Resource Sufficiency
-   **What:** Before making a drink, the program must check if there are enough ingredients in the `resources` dictionary.
-   **How:** I created a function `is_resource_sufficient(order_ingredients)`. This function loops through the required ingredients for the chosen drink and compares them to the machine's current `resources`. It returns `False` and prints a warning if any ingredient is insufficient, otherwise it returns `True`.

#### Feature 3: Process Coins
-   **What:** The machine needs to ask the user for the number of quarters, dimes, nickels, and pennies they are inserting.
-   **How:** I built a function `process_coins()` that prompts the user for the quantity of each coin type. It then calculates the total monetary value and `return`s it. This kept the coin logic separate and clean.

#### Feature 4: Check Transaction Success
-   **What:** After processing coins, the program must verify if the total amount is enough to cover the cost of the drink.
-   **How:** I created another function, `is_transaction_successful(money_received, drink_cost)`.
    -   If the money is not enough, it prints a refund message and returns `False`.
    -   If the money is sufficient, it adds the drink's cost to the `profit`, calculates and prints any change due, and returns `True`. I had to use the `global` keyword to modify the `profit` variable.

#### Feature 5: Make Coffee & Deduct Resources
-   **What:** If resources are sufficient and the transaction is successful, the machine "makes" the coffee. This involves deducting the used ingredients from the `resources`.
-   **How:** I made a final function, `make_coffee(drink_name, order_ingredients)`. It iterates through the ingredients of the ordered drink and subtracts the required amounts from the `resources` dictionary. Finally, it prints a message telling the user to enjoy their drink.

---

### 3. My Approach and Code Structure
To build this, I followed a structured approach:

1.  **Global Data:** I started with the provided `MENU` and `resources` dictionaries defined at the global level, along with a `profit` variable initialized to 0.
2.  **Main Loop:** The entire program runs inside a `while is_on:` loop, which continuously prompts the user for input.
3.  **Command Handling:** Inside the loop, I used an `if/elif/else` structure to handle the different user inputs ("off", "report", or a drink name).
4.  **Modular Functions:** I broke down each major task into its own function (`is_resource_sufficient`, `process_coins`, `is_transaction_successful`, `make_coffee`). This made the main loop clean and easy to read, as it just called these functions in the correct order. Each function had a specific job and returned a value (like `True`/`False` or a total amount) that determined the next step in the logic.

---

### 4. Final Project Code: The Coffee Machine
Here is the complete and final code for my Coffee Machine project.

```python
# main.py
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
```