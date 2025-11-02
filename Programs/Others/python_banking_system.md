# My Journey Building a Python Banking System

Hello! Welcome to the detailed walkthrough of the banking system I built. This wasn't just about writing code; it was an exercise in thinking like an architect, starting with a simple foundation and adding complex features layer by layer. In this document, I'm going to explain my entire thought process—the "what," the "why," and the "how"—for each level of the project. I'll cover the data structures I chose, the logic behind the functions, the real-world scenarios they're meant to simulate, and finally, the complete, commented code.

Let's dive in!

## Table of Contents
- [Core Concepts: The Big Picture](#core-concepts)
- [Level 1: The Foundation - Accounts, Deposits, and Transfers](#level-1)
- [Level 2: Tracking Spending - Who Are the Top Spenders?](#level-2)
- [Level 3: Advanced Features - Scheduled Payments & Cashback](#level-3)
- [Level 4: The Endgame - Merging Accounts & Time Travel](#level-4)
- [Final Thoughts](#final-thoughts)
- [The Complete Code with Explanations](#the-code)

---

### Core Concepts: The Big Picture
<a name="core-concepts"></a>

Before we get into the code for each level, let's talk about the fundamental ideas that underpin the entire system.

#### Why an Object-Oriented Approach?
I decided to wrap everything in a `BankingSystemImpl` class. Why? Because a banking system has *state*. It needs to remember all the accounts, their balances, and transaction histories. A class is the perfect way to hold all that data (like `self.accounts`, `self.payments`, etc.) and the methods that operate on that data (`deposit`, `transfer`, etc.) together in one neat, organized package. It's like a digital bank building that holds all the vaults (the data) and employs all the tellers (the methods). Without a class, I'd have to manage all this information with global variables, which would get messy and hard to maintain very quickly.

#### The Importance of Timestamps
You'll notice every single function takes a `timestamp` as its first argument. The problem guarantees that these are unique and always increasing. This is a massive simplification, but it's the bedrock of the entire system. In the real world, transactions can sometimes arrive out of order, and handling that is a huge challenge. But here, we can rely on this guarantee. It allows us to:
1.  **Process events in order:** We never have to worry about a transaction from "tomorrow" arriving before one from "today." This makes our logic much simpler.
2.  **Create historical records:** By tagging every balance change with a timestamp, we can later figure out what an account's balance was at any point in the past. This is the magic behind Level 4's `get_balance` feature. It's like every page in a bank's ledger has a precise date and time written on it.

#### My Digital Ledger: The `self.accounts` Dictionary
The heart of the bank is the `self.accounts` dictionary. It's a simple but incredibly powerful choice.
-   **The Key:** The `account_id` (a string). This gives me instant, O(1) or constant time, lookup for any account. No need to loop through a list to find someone, which would be much slower (O(n) time).
-   **The Value:** Another dictionary! This nested dictionary holds everything about a single account: its `balance`, its total `outgoing` transaction amount, the `timestamp` it was created at, and a `history` of its balance changes.

It looks something like this in memory:
```python
self.accounts = {
    "account1": {
        "balance": 1500,
        "outgoing": 500,
        "created_at": 100,
        "history": [(101, 2000), (105, 1500)]
    },
    "account2": { ... }
}
```

---

### Level 1: The Foundation - Accounts, Deposits, and Transfers
<a name="level-1"></a>

**The Goal:** To build the absolute bare minimum functionality of a bank. People need to be able to open accounts, put money in, and send money to others.

#### How I Built It:
1.  **`create_account(timestamp, account_id)`:** This is the front door of our bank. The logic is simple: first, I check if an account with that `account_id` already exists in my `self.accounts` ledger. If it does, I can't create a duplicate, so I return `False`. This is a critical real-world validation step. If it's a new customer, I create a new entry for them, initializing their balance and outgoing amount to zero.

2.  **`deposit(timestamp, account_id, amount)`:** This is probably the simplest operation. I just look up the `account_id` in my ledger. If the account doesn't exist, I can't deposit money into it, so I return `None`. If it does exist, I simply add the `amount` to the account's `balance`.

3.  **`transfer(timestamp, source_account_id, target_account_id, amount)`:** This is where things get more interesting because a single action affects two accounts and has multiple failure points, just like a real bank transfer. I implemented a chain of checks in a specific order for safety and efficiency:
    -   First, do both the source and target accounts actually exist? If not, the transaction is impossible.
    -   Next, is the user trying to send money to themselves? The rules say this isn't allowed.
    -   Finally, the most important check: does the source account have enough money? This is the insufficient funds check (`source_account['balance'] < amount`).
    -   If all those checks pass, and only then, do I perform the transaction: subtract the `amount` from the source's balance and add it to the target's balance. This two-step process is "atomic" in our simulation—it either happens completely or not at all.

---

### Level 2: Tracking Spending - Who Are the Top Spenders?
<a name="level-2"></a>

**The Goal:** The bank wants some basic business intelligence. They want to identify accounts that have the highest amount of outgoing money. This could be for a rewards program, or for risk analysis.

#### How I Built It:
1.  **Adding the `outgoing` Tracker:** The first step was to actually track this metric. I made sure that whenever a new account is created, its dictionary includes `'outgoing': 0`.

2.  **Updating `transfer`:** A "spending" event happens during a transfer. So, I updated the `transfer` method. When a transfer is successful, I now also add the `amount` to the `source_account`'s `'outgoing'` value. It's a simple accumulator.

3.  **The `top_spenders(timestamp, n)` Method:** This is where the magic happens.
    -   I get all the accounts from my `self.accounts` ledger.
    -   I then use Python's built-in `sorted()` function. This function is incredibly powerful because you can give it a `key` to tell it *how* to sort things.
    -   My key was a `lambda` function: `key=lambda item: (-item[1]['outgoing'], item[0])`. This looks complex, but it's quite simple. It tells Python: "For each account, create a tuple of two values to sort by. The first value is the *negative* of their outgoing amount. The second value is their account ID."
    -   **Why the negative?** `sorted()` sorts in ascending order by default (smallest to largest). By sorting on the negative of the outgoing amount, I trick it into sorting the actual amounts in *descending* order (e.g., -5000 comes before -100).
    -   **The Tie-Breaker:** The second part of the tuple, the `account_id` (`item[0]`), is for breaking ties. If two accounts have the same outgoing amount (e.g., 1500), Python will then look at the second value in the tuple and sort them alphabetically (e.g., 'accountA' comes before 'accountB'). This ensures a consistent, predictable order.
    -   Finally, I just take the top `n` results from this sorted list and format them into the required string format, like `"account1(5000)"`.

---

### Level 3: Advanced Features - Scheduled Payments & Cashback
<a name="level-3"></a>

**The Goal:** Now we're entering the world of more complex financial products. We need to handle payments that trigger a future event: a cashback deposit that arrives exactly 24 hours later.

#### How I Built It:
This level required a new way of thinking about time.

1.  **`pay(timestamp, account_id, amount)`:** This function is similar to a transfer, but it's only outgoing. It checks for the account and sufficient funds. If successful, it does two key things:
    -   It deducts the `amount` from the balance and adds it to the `outgoing` total.
    -   It *schedules* the cashback. It calculates the cashback amount (2% rounded down) and the exact `cashback_timestamp` (current `timestamp` + 24 hours in milliseconds).

2.  **The To-Do List: `self.pending_cashbacks`:** I created a new list to act as my scheduler or to-do list. When a payment is made, I add a tuple to this list: `(cashback_timestamp, account_id, cashback_amount, payment_id)`. Because new events always have a later timestamp, this list naturally stays sorted by when the cashback is due. This is a crucial property.

3.  **The Engine: `_process_cashbacks(current_timestamp)`:** This is the most important new piece of logic. It's a helper function (I prefixed it with `_` to denote it's for internal use) that I call at the **very beginning** of every single other method (`create_account`, `deposit`, `pay`, etc.).
    -   Its job is to look at the `self.pending_cashbacks` list and check if any scheduled cashbacks are now due (i.e., their `cashback_timestamp` is less than or equal to the `current_timestamp` of the operation being performed).
    -   If it finds any, it processes them: it adds the cashback amount to the correct account's balance, updates the payment's status to "CASHBACK_RECEIVED," and then removes it from the pending list.
    -   By running this check *before* any action, I guarantee that the bank's state is always fully up-to-date before a new transaction is even considered. It’s a simple and effective way to handle these delayed, time-based events.

4.  **`get_payment_status(...)`:** This required another dictionary, `self.payments`, to track the status of each payment. When a payment is created in the `pay` method, I add an entry here with the status "IN_PROGRESS". When `_process_cashbacks` does its job, it finds this payment and flips the status to "CASHBACK_RECEIVED". This function just looks up the status in that dictionary after running the cashback processor.

---

### Level 4: The Endgame - Merging Accounts & Time Travel
<a name="level-4"></a>

**The Goal:** This is the most complex level, introducing two major features: consolidating two accounts into one, and being able to look up an account's balance at any point in the past.

#### How I Built It:
1.  **Adding a `history` List:** To enable "time travel," I first needed a time machine. I modified `create_account` to give every new account an empty `'history': []` list. Then, in every method that changed an account's balance (`deposit`, `transfer`, `pay`, and even `_process_cashbacks`), I added a line to append a new tuple `(timestamp, new_balance)` to that account's history list. Now I had a complete, timestamped log of every balance change for every account.

2.  **`get_balance(timestamp, account_id, time_at)`:** The Time Machine itself!
    -   It takes a `time_at` parameter, which is the historical point in time we're interested in.
    -   It finds the account's `history` list. This list is a sorted record of balance changes.
    -   To find the balance at `time_at`, I need to find the *last* recorded balance change that happened *on or before* `time_at`.
    -   Doing a linear search would be slow for a long history. So, I used Python's `bisect` module. `bisect.bisect_right` is a highly-optimized function that uses a binary search to very quickly find the correct insertion point for `time_at` in my list of timestamps. The item just before this insertion point is the historical record I'm looking for! It's efficient and elegant.

3.  **`merge_accounts(...)`:** This was tricky. My first instinct was just to dump everything from account 2 into account 1 and delete account 2. But that was a mistake, as the automated tests showed.
    -   **The Mistake:** Deleting account 2 meant I lost its history forever. If a user asked for the balance of account 2 *before* it was merged, my system would say it never existed. That's incorrect. A real bank can't just pretend a closed account never existed; they have to keep records.
    -   **The Fix: The `deleted_accounts` Archive:** Instead of truly deleting the account, I created a new dictionary called `self.deleted_accounts`. When `merge_accounts` is called, I move the entire dictionary for `account_id_2` from `self.accounts` into this archive. I also add a `'merged_at'` timestamp to it.
    -   **The Logic:**
        -   The final balance and total `outgoing` from account 2 are added to account 1.
        -   All of account 2's pending cashbacks and past payments are reassigned to be owned by account 1.
        -   Account 2 is moved to the archive.
    -   **The `get_balance` Update:** My `get_balance` function now checks three places. First, the active `self.accounts`. If not found, it checks the `self.deleted_accounts` archive. If it finds it there, it can still use its history, but with one crucial check: if the user is asking for a balance at a time (`time_at`) *after* the account was merged, it correctly returns `None`, because at that point in time, the account really didn't exist anymore.

---

### Final Thoughts
<a name="final-thoughts"></a>

This project was a fantastic simulation of real-world software development. It started simple and grew in complexity, forcing me to refactor and rethink my data structures along the way (like realizing I needed a `deleted_accounts` archive instead of a simple `del`). It highlighted the importance of handling state, processing events in order, and planning for future requirements. The use of simple Python dictionaries and lists, combined with powerful modules like `bisect`, shows that you can build complex, logical systems with clean, readable code.

---

### The Complete Code with Explanations
<a name="the-code"></a>

Here is the full, final implementation of the `BankingSystemImpl` class, with comments explaining each part of the code.

```python
from banking_system import BankingSystem
import math
import bisect

class BankingSystemImpl(BankingSystem):
    """
    Provides the concrete implementation for the BankingSystem interface.
    This class manages all accounts, payments, and transactions.
    """
    def __init__(self):
        """
        Initializes the banking system. We set up all the data structures
        that will hold the state of our bank.
        """
        # The main ledger for all active accounts.
        # Key: account_id, Value: dictionary of account details.
        self.accounts = {}
        
        # A simple counter to ensure every payment gets a unique ID.
        self.payment_counter = 0
        
        # A ledger for all payments made.
        # Key: payment_id, Value: dictionary of payment details.
        self.payments = {}
        
        # A sorted list that acts as a scheduler for future cashback events.
        self.pending_cashbacks = []
        
        # A constant for 24 hours in milliseconds for cashback calculations.
        self.MILLISECONDS_IN_24_HOURS = 24 * 60 * 60 * 1000
        
        # An archive for accounts that have been merged. We don't delete them
        # completely so we can query their history.
        self.deleted_accounts = {}

    def _process_cashbacks(self, current_timestamp: int):
        """
        (Internal Helper) Processes any pending cashbacks that are due by the current_timestamp.
        This is the engine of our time-based events system. It's called at the
        start of every public method to ensure the bank's state is always up-to-date.
        """
        processed_cashbacks = []
        for cashback in self.pending_cashbacks:
            # Check if the cashback's due time is in the past or present.
            if cashback[0] <= current_timestamp:
                processed_cashbacks.append(cashback)
            else:
                # The list is sorted, so we can stop searching as soon as we
                # find a cashback scheduled for the future.
                break
        
        if not processed_cashbacks:
            return

        # Process all due cashbacks.
        for cashback in processed_cashbacks:
            cashback_ts, account_id, amount, payment_id = cashback
            if account_id in self.accounts:
                account = self.accounts[account_id]
                account['balance'] += amount
                # Record this deposit in the account's history.
                account['history'].append((cashback_ts, account['balance']))
            
            # Update the payment status from "IN_PROGRESS".
            self.payments[payment_id]['status'] = "CASHBACK_RECEIVED"
            
        # Remove the processed cashbacks from the pending list efficiently.
        self.pending_cashbacks = self.pending_cashbacks[len(processed_cashbacks):]

    def create_account(self, timestamp: int, account_id: str) -> bool:
        self._process_cashbacks(timestamp)
        if account_id in self.accounts:
            return False
        
        # Initialize a new account with default values.
        self.accounts[account_id] = {
            'balance': 0,
            'outgoing': 0,
            'created_at': timestamp,
            'history': [] # Initialize an empty history log.
        }
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        self._process_cashbacks(timestamp)
        if account_id not in self.accounts:
            return None
        
        account = self.accounts[account_id]
        account['balance'] += amount
        # Log this transaction in the account's history.
        account['history'].append((timestamp, account['balance']))
        return account['balance']

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        self._process_cashbacks(timestamp)
        # Validation checks
        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return None
        if source_account_id == target_account_id:
            return None
            
        source_account = self.accounts[source_account_id]
        
        if source_account['balance'] < amount:
            return None # Insufficient funds.
            
        target_account = self.accounts[target_account_id]
        
        # Perform the atomic transaction
        source_account['balance'] -= amount
        source_account['outgoing'] += amount
        target_account['balance'] += amount
        
        # Log the balance change for both accounts.
        source_account['history'].append((timestamp, source_account['balance']))
        target_account['history'].append((timestamp, target_account['balance']))
        
        return source_account['balance']
        
    def pay(self, timestamp: int, account_id: str, amount: int) -> str | None:
        self._process_cashbacks(timestamp)
        if account_id not in self.accounts:
            return None
            
        account = self.accounts[account_id]
        if account['balance'] < amount:
            return None
            
        # Process payment
        account['balance'] -= amount
        account['outgoing'] += amount
        account['history'].append((timestamp, account['balance']))
        
        # Generate unique payment ID
        self.payment_counter += 1
        payment_id = f"payment{self.payment_counter}"
        
        # Schedule cashback
        cashback_amount = int(amount * 0.02) # Rounded down
        cashback_timestamp = timestamp + self.MILLISECONDS_IN_24_HOURS

        # Log the payment details.
        self.payments[payment_id] = {
            'account_id': account_id,
            'status': "IN_PROGRESS"
        }
        
        # Add to our scheduler if there is a cashback amount.
        if cashback_amount > 0:
            self.pending_cashbacks.append(
                (cashback_timestamp, account_id, cashback_amount, payment_id)
            )
            # Ensure the list remains sorted after adding a new item.
            self.pending_cashbacks.sort()
        else:
            self.payments[payment_id]['status'] = "CASHBACK_RECEIVED"

        return payment_id

    def get_payment_status(self, timestamp: int, account_id: str, payment: str) -> str | None:
        self._process_cashbacks(timestamp)
        if account_id not in self.accounts:
            return None
        if payment not in self.payments:
            return None
        if self.payments[payment]['account_id'] != account_id:
            return None
            
        return self.payments[payment]['status']

    def top_spenders(self, timestamp: int, n: int) -> list[str]:
        self._process_cashbacks(timestamp)
        all_accounts = list(self.accounts.items())

        # Sort by outgoing amount (desc) and then account_id (asc) for ties.
        sorted_accounts = sorted(
            all_accounts,
            key=lambda item: (-item[1]['outgoing'], item[0])
        )

        top_n_accounts = sorted_accounts[:n]

        # Format the output strings.
        return [f"{acc_id}({details['outgoing']})" for acc_id, details in top_n_accounts]

    def merge_accounts(self, timestamp: int, account_id_1: str, account_id_2: str) -> bool:
        self._process_cashbacks(timestamp)
        if account_id_1 == account_id_2:
            return False
        if account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False
            
        acc1 = self.accounts[account_id_1]
        acc2 = self.accounts[account_id_2]

        # Consolidate balances and spending history.
        acc1['balance'] += acc2['balance']
        acc1['outgoing'] += acc2['outgoing']

        # Add a single entry to acc1's history for the merge transaction.
        acc1['history'].append((timestamp, acc1['balance']))

        # Re-assign pending cashbacks from acc2 to acc1.
        self.pending_cashbacks = [
            (ts, account_id_1 if acc_id == account_id_2 else acc_id, amt, p_id)
            for ts, acc_id, amt, p_id in self.pending_cashbacks
        ]
        self.pending_cashbacks.sort() # Re-sort after modification.

        # Re-assign payment ownership from acc2 to acc1.
        for payment_id, payment_info in self.payments.items():
            if payment_info['account_id'] == account_id_2:
                payment_info['account_id'] = account_id_1
                
        # Move the second account to the archive.
        self.deleted_accounts[account_id_2] = acc2
        self.deleted_accounts[account_id_2]['merged_at'] = timestamp
        del self.accounts[account_id_2]
        
        return True

    def get_balance(self, timestamp: int, account_id: str, time_at: int) -> int | None:
        self._process_cashbacks(timestamp)

        account = None
        # Check active accounts first.
        if account_id in self.accounts:
            account = self.accounts[account_id]
        # If not active, check the archive of merged accounts.
        elif account_id in self.deleted_accounts:
            account = self.deleted_accounts[account_id]
            # An archived account doesn't exist *after* it was merged.
            if 'merged_at' in account and time_at >= account['merged_at']:
                return None
        else:
            return None # The account never existed.

        # An account has no balance before it was created.
        if time_at < account['created_at']:
            return None
        
        history = account['history']
        # History can become unsorted if a cashback from a merged account is processed.
        # We sort here as a safeguard to ensure bisect works correctly.
        history.sort(key=lambda x: x[0])
        timestamps = [h[0] for h in history]
        
        # Use binary search to find the index of the last transaction
        # that occurred on or before `time_at`.
        idx = bisect.bisect_right(timestamps, time_at)
        
        if idx == 0:
            # No transactions occurred at or before this time.
            return 0
        else:
            # The balance is the value from the transaction at the found index - 1.
            return history[idx - 1][1]

```
Thanks for reading through my journey!