# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 92 - BankAccount class

"""
Write a class BankAccount that allows us to manage a bank account.
This class will have two attributes: name and balance.
By default, the attributes have the following values: name = "Maxime",
balance = 600.

This class should include the following three methods:
        - deposit(self, amount) which will add a certain amount
          to the balance.
        - withdraw(self, amount) which will withdraw a certain amount
          from the balance.
        - __repr__(self) which will display the account holder's name
          and the balance of their account.

Verification tests:
>> account1 = BankAccount("Julie", 1000)
>> account1.deposit(400)
>> account1.withdraw(100)
>> account1
The balance of Julie's bank account is 1300 euros.

>> account2 = BankAccount()
>> account2.deposit(500)
>> account2
The balance of Maxime's bank account is 1100 euros.
"""

class BankAccount:
    def __init__(self, name="Maxime", balance=600):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        self.balance -= float(amount)

    def __repr__(self):
        return f"The balance of {self.name}'s bank account is {self.balance:.0f} euros."


# -------------------- TEACHING NOTES --------------------
# Topic: Modeling a Simple Bank Account
#
# 1. Why default values?
#    Allows creating an account with no arguments (account2 in the example).
#
# 2. Why convert balance/amount to float?
#    Ensures consistent numeric behavior even if integers are passed.
#
# 3. Why use __repr__?
#    Makes printing the object show a human-readable summary.
#
# 4. Why no validation?
#    The exercise does not require preventing negative balances.


# -------------------- EXAMPLES --------------------
#
# >>> a = BankAccount("Julie", 1000)
# >>> a.deposit(400)
# >>> a.withdraw(100)
# >>> a
# The balance of Julie's bank account is 1300 euros.
#
# >>> b = BankAccount()
# >>> b.deposit(500)
# >>> b
# The balance of Maxime's bank account is 1100 euros.


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Misspelling deposit as "deposti" (typo in the prompt).
# 2. Forgetting to convert amount to float.
# 3. Forgetting to return a string in __repr__.
# 4. Using print() inside __repr__ instead of returning a value.
# 5. Overthinking validation (not required here).


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class BankAccount_Beginner:
    def __init__(self, name="Maxime", balance=600):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        new_balance = self.balance + float(amount)
        self.balance = new_balance

    def withdraw(self, amount):
        new_balance = self.balance - float(amount)
        self.balance = new_balance

    def __repr__(self):
        return f"The balance of {self.name}'s bank account is {self.balance:.0f} euros."


# Intermediate Version 
class BankAccount_Intermediate:
    def __init__(self, name="Maxime", balance=600):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        self.balance -= float(amount)

    def __repr__(self):
        return f"The balance of {self.name}'s bank account is {self.balance:.0f} euros."


# Advanced Version (adds validation + properties)
class BankAccount_Advanced:
    def __init__(self, name="Maxime", balance=600):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.name = name
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += float(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= float(amount)

    def __repr__(self):
        return f"The balance of {self.name}'s bank account is {self._balance:.0f} euros."


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using default parameter values.
# 2. Modeling real-world entities with attributes + methods.
# 3. Using __repr__ for readable object output.
# 4. Adding validation in advanced versions.
# 5. Using @property to protect internal state.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does __repr__ do?
# A1: Returns a string representation of the object.
#
# Q2: Why use default values in __init__?
# A2: Allows creating objects without passing arguments.
#
# Q3: What happens if you deposit a string like "50"?
# A3: It works because float("50") converts it.
#
# Q4: What does the advanced version prevent?
# A4: Negative balances, negative deposits, and invalid withdrawals.
#
# ---------------------------------------------------------------
