# 100 Exercises for Practicing PYTHON
# Author: Laurentine K. Masson
# Advanced-level exercises
# Code Solution Written by: Jose "Joe" Ruiz

# Exercise 93 - Car class

"""
Write a class Car that allows us to manage rental automobiles. The class
will have 4 attributes representing various characteristics: brand, color,
driverName and startingKm.
By default, these attributes have the following values:
brand = "peugeot", color = "dark", driverName = "None", startingKm = 16900

This class should include the following three methods:
        - chooseDriver(self, driverName) which will designate or change
          the driver's name for the car.
        - calculateDistance(self, finalKm) which will calculate the distance
          traveled by the driver during the rental period.
        - displayInfo(self) which will display the current state of the car,
          including the driver's name, brand, color, and current mileage.

Verification tests:
>> car1 = Car()
>> car1.chooseDriver("Patrick")
>> car1.calculateDistance(20000)
3100
>> car1.displayInfo()
The black Peugeot car driven by Patrick currently has a mileage of 20000 Km.
"""

class Car:
    def __init__(self, brand="peugeot", color="dark", driverName="None", startingKm=16900):
        self.brand = brand
        self.color = color
        self.driverName = driverName
        self.startingKm = int(startingKm)

    def chooseDriver(self, driverName):
        self.driverName = driverName

    def calculateDistance(self, finalKm):
        finalKm = int(finalKm)
        distance = finalKm - self.startingKm
        self.startingKm = finalKm
        return distance

    def displayInfo(self):
        return (
            f"The {self.color} {self.brand.capitalize()} car driven by "
            f"{self.driverName} currently has a mileage of {self.startingKm} Km."
        )


# -------------------- TEACHING NOTES --------------------
# Topic: Modeling Rental Cars with Classes
#
# 1. Why default values?
#    Allows creating a Car() with no arguments, matching the exercise tests.
#
# 2. Why store startingKm as int?
#    Mileage is always a whole number.
#
# 3. Why update startingKm inside calculateDistance?
#    Because the car's mileage should reflect the new finalKm after the rental.
#
# 4. Why use brand.capitalize()?
#    Ensures output formatting matches the example ("Peugeot").


# -------------------- EXAMPLES --------------------
#
# >>> car1 = Car()
# >>> car1.chooseDriver("Patrick")
# >>> car1.calculateDistance(20000)
# 3100
#
# >>> car1.displayInfo()
# "The dark Peugeot car driven by Patrick currently has a mileage of 20000 Km."
#
# >>> car2 = Car("toyota", "white", "Sarah", 5000)
# >>> car2.calculateDistance(5500)
# 500
# >>> car2.displayInfo()
# "The white Toyota car driven by Sarah currently has a mileage of 5500 Km."


# -------------------- COMMON PITFALLS & GOTCHAS --------------------
#
# 1. Forgetting to update startingKm after calculating distance.
# 2. Returning the wrong value from calculateDistance.
# 3. Misspelling attribute names (driverName vs drivername).
# 4. Forgetting to capitalize brand in displayInfo.
# 5. Using print() instead of return in displayInfo.


# -------------------- BEGINNER vs. INTERMEDIATE vs. ADVANCED --------------------

# Beginner Version (very explicit)
class Car_Beginner:
    def __init__(self, brand="peugeot", color="dark", driverName="None", startingKm=16900):
        self.brand = brand
        self.color = color
        self.driverName = driverName
        self.startingKm = int(startingKm)

    def chooseDriver(self, driverName):
        self.driverName = driverName

    def calculateDistance(self, finalKm):
        finalKm = int(finalKm)
        distance = finalKm - self.startingKm
        self.startingKm = finalKm
        return distance

    def displayInfo(self):
        info = (
            f"The {self.color} {self.brand.capitalize()} car driven by "
            f"{self.driverName} currently has a mileage of {self.startingKm} Km."
        )
        return info


# Intermediate Version (my implementation)
class Car_Intermediate:
    def __init__(self, brand="peugeot", color="dark", driverName="None", startingKm=16900):
        self.brand = brand
        self.color = color
        self.driverName = driverName
        self.startingKm = int(startingKm)

    def chooseDriver(self, driverName):
        self.driverName = driverName

    def calculateDistance(self, finalKm):
        finalKm = int(finalKm)
        distance = finalKm - self.startingKm
        self.startingKm = finalKm
        return distance

    def displayInfo(self):
        return (
            f"The {self.color} {self.brand.capitalize()} car driven by "
            f"{self.driverName} currently has a mileage of {self.startingKm} Km."
        )


# Advanced Version (adds validation + properties)
class Car_Advanced:
    def __init__(self, brand="peugeot", color="dark", driverName="None", startingKm=16900):
        if int(startingKm) < 0:
            raise ValueError("Mileage cannot be negative.")
        self.brand = brand
        self.color = color
        self.driverName = driverName
        self._startingKm = int(startingKm)

    @property
    def startingKm(self):
        return self._startingKm

    def chooseDriver(self, driverName):
        if not driverName:
            raise ValueError("Driver name cannot be empty.")
        self.driverName = driverName

    def calculateDistance(self, finalKm):
        finalKm = int(finalKm)
        if finalKm < self._startingKm:
            raise ValueError("Final mileage cannot be less than starting mileage.")
        distance = finalKm - self._startingKm
        self._startingKm = finalKm
        return distance

    def displayInfo(self):
        return (
            f"The {self.color} {self.brand.capitalize()} car driven by "
            f"{self.driverName} currently has a mileage of {self._startingKm} Km."
        )


# -------------------- PATTERNS TO RECOGNIZE --------------------
#
# 1. Using default values for flexible object creation.
# 2. Updating internal state after calculations.
# 3. Using methods to encapsulate behavior.
# 4. Adding validation in advanced versions.
# 5. Using @property to protect internal attributes.


# -------------------- MINI-QUIZ (ACTIVE RECALL) --------------------
#
# Q1: What does calculateDistance return?
# A1: finalKm - startingKm.
#
# Q2: Why update startingKm after calculating distance?
# A2: To reflect the car's new mileage.
#
# Q3: What does chooseDriver do?
# A3: Assigns or changes the driverName attribute.
#
# Q4: Why capitalize the brand in displayInfo?
# A4: To match proper noun formatting ("Peugeot").
#
# ---------------------------------------------------------------
