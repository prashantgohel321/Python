# Task 2: Object-Oriented Programming - The Vending Machine

This was a much more challenging task because it forced us to think in terms of **Object-Oriented Programming (OOP)**. Instead of just writing a function, we had to build a virtual machine that maintains a **state** and responds to events (like a purchase attempt). I love these problems because they model the real world perfectly!

---

## What We Did: Building a Class

We defined a Python **class** named `VendingMachine`. A class is essentially a blueprint for creating objects. Our object needed two core parts:

1.  **State (The Inventory):** What does the machine know about itself? The current number of items and the price per item.
2.  **Behavior (The Transaction):** What can the machine *do*? It can process a `buy` request.

## Why This Matters: State and Exceptions

### Why Use a Class (`class VendingMachine`)?

Imagine you had 10 vending machines. If you just used a simple function, how would you track the stock for each one? You'd have to pass the stock count back and forth every time. By using a class, we create an **instance** (an actual machine) that *holds its own data*. If machine A sells 5 items, machine B's stock isn't affected. That's the power of OOP!

### Why Use Exceptions (`raise ValueError`)?

This is the most critical part of the solution. When you use a real vending machine, and something goes wrong (e.g., it's empty), it doesn't just return a number like `-1`; it displays a clear error message.

We use `raise ValueError("Not enough items in the machine")` because:

* **Clarity:** It immediately stops the transaction and communicates *exactly* what went wrong.
* **Separation of Concerns:** The `buy` method focuses only on **checking and processing**. The code calling `buy` (the test harness) is responsible for **handling** the error using a `try...except` block, which is much cleaner.

## How We Did It: The `__init__` and `buy` Methods

### 1. The Setup (`__init__`)

The `__init__` method is like the machine's factory setup. When we initialize the machine (`machine = VendingMachine(10, 2)`), this is where we store the starting inventory and price in the machine itself:

```python
def __init__(self, num_items, item_price):
    self.num_items = num_items   # Our current stock
    self.item_price = item_price # Our price tag
```

The `self.` prefix is essential—it tells Python that these variables belong to *this specific VendingMachine object*.

### 2. The Transaction Logic (`buy`)

The `buy` method is where the machine acts like a responsible business owner, checking its limits before committing to a sale. The order of checks is very important:

#### A. Calculate Cost

First, we figure out the total damage:
`total_cost = req_items * self.item_price`

#### B. Check Stock (The First Gate)

We check if the customer is asking for more than we have. This must come first. If the shelf is empty, the money doesn't matter!

```python
if req_items > self.num_items:
    raise ValueError("Not enough items in the machine")
```

#### C. Check Funds (The Second Gate)

If we have the items, we check the money.

```python
if money < total_cost:
    raise ValueError("Not enough coins")
```

#### D. Success! (Update State)

Only if both checks pass do we complete the sale. We calculate the change, update the machine's internal stock, and send the change back to the customer.

```python
change = money - total_cost
self.num_items -= req_items # Stock reduced!
return change
```

This clean structure ensures that the machine state (`self.num_items`) is only ever changed when a transaction is guaranteed to be successful, preventing accidental errors and keeping the inventory accurate.
