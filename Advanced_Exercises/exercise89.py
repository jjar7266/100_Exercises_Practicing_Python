# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 89 - Creating a class Person

"""
Create a Python class named Person that processes three attributes
defining certain characteristics of a real person: height(in m), weight
(in kg) and age.

This Python class will have two methods:
        - calculateBMI(self) which calculates the BMI of the person.
        - interpretBMI(self) which displays:
                * "The BMI calculation indicates that the person is
                underweight (thinness)" if the result returned by
                calculateBMI(self) is less than or equal to 18.5.
                * "The person is obese" if the result is greater than or
                equal to 30.
                * Otherwise, it displays "The person is overweight or has a
                normal body weight"

Reminder: The Body Mass Index (BMI) is calculated using the formula
weight/(height**2).

Verification tests:
>> julien = Person(1.87, 95, 26)
>> julien.calculateBMI()
27.16
>> julien.interpretBMI()
"The person is overweight or has a normal body weight"
"""


class Person:
    def __init__(self, height, weight, age):
        self.height = float(height)
        self.weight = float(weight)
        self.age = int(age)

    def calculateBMI(self):
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    def interpretBMI(self):
        bmi = self.calculateBMI()

        if bmi <= 18.5:
            return "The BMI calculation indicates that the person is underweight (thinness)"
        elif bmi >= 30:
            return "The person is obese"
        else:
            return "The person is overweight or has a normal body weight"


# -------------------- TEACHING NOTES --------------------
# Topic: Object-Oriented Programming (OOP) – Modeling a Person
#
# 1. Why use a class?
#    A class groups related data (height, weight, age) and behavior (BMI methods).
#
# 2. Why round BMI?
#    BMI is normally reported to 1–2 decimal places.
#
# 3. Why use self?
#    self refers to the specific instance (the specific person).
#
# 4. Why separate calculateBMI() and interpretBMI()?
#    - calculateBMI() handles math
#    - interpretBMI() handles logic and messaging
#    This separation keeps the code clean and testable.


# -------------------- EXAMPLES --------------------
#
# >>> julien = Person(1.87, 95, 26)
# >>> julien.calculateBMI()
# 27.16
#
# >>> julien.interpretBMI()
# "The person is overweight or has a normal body weight"
#
# >>> Person(1.60, 45, 20).interpretBMI()
# "The BMI calculation indicates that the person is underweight (thinness)"
#
# >>> Person(1.70, 105, 40).interpretBMI()
# "The person is obese"


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to convert height/weight to float.
# 2. Forgetting to round BMI (raw floats can be messy).
# 3. Using height in cm instead of meters.
# 4. Misplacing the BMI thresholds (<= 18.5, >= 30).
# 5. Calling calculateBMI(self) instead of calculateBMI().


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit, minimal abstraction)
class Person_Beginner:
    def __init__(self, height, weight, age):
        self.height = float(height)
        self.weight = float(weight)
        self.age = int(age)

    def calculateBMI(self):
        bmi = self.weight / (self.height * self.height)
        return round(bmi, 2)

    def interpretBMI(self):
        bmi = self.calculateBMI()
        if bmi <= 18.5:
            return "The BMI calculation indicates that the person is underweight (thinness)"
        if bmi >= 30:
            return "The person is obese"
        return "The person is overweight or has a normal body weight"


# Intermediate Version (My implementation)
class Person_Intermediate:
    def __init__(self, height, weight, age):
        self.height = float(height)
        self.weight = float(weight)
        self.age = int(age)

    def calculateBMI(self):
        return round(self.weight / (self.height ** 2), 2)

    def interpretBMI(self):
        bmi = self.calculateBMI()
        if bmi <= 18.5:
            return "The BMI calculation indicates that the person is underweight (thinness)"
        elif bmi >= 30:
            return "The person is obese"
        else:
            return "The person is overweight or has a normal body weight"


# Advanced Version (adds validation + categorization method)
class Person_Advanced:
    def __init__(self, height, weight, age):
        if height <= 0:
            raise ValueError("Height must be positive.")
        if weight <= 0:
            raise ValueError("Weight must be positive.")
        if age <= 0:
            raise ValueError("Age must be positive.")

        self.height = float(height)
        self.weight = float(weight)
        self.age = int(age)

    def calculateBMI(self):
        return round(self.weight / (self.height ** 2), 2)

    def bmiCategory(self, bmi):
        if bmi <= 18.5:
            return "underweight (thinness)"
        elif bmi >= 30:
            return "obese"
        else:
            return "overweight or normal body weight"

    def interpretBMI(self):
        bmi = self.calculateBMI()
        return f"The person is {self.bmiCategory(bmi)}"


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Modeling real-world entities with classes.
# 2. Using methods to compute and interpret data.
# 3. Separating logic (BMI math vs. BMI interpretation).
# 4. Using validation in advanced versions.
# 5. Returning strings instead of printing (more flexible).


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What is the BMI formula?
# A1: weight / (height ** 2)
#
# Q2: What BMI value is considered obese?
# A2: BMI >= 30
#
# Q3: Why round the BMI?
# A3: To avoid long floating‑point decimals.
#
# Q4: Why use a class for this exercise?
# A4: To group related attributes and behaviors into one object.
#
# ---------------------------------------------------------------
