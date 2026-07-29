# ============================================================
# Python: Object-Oriented Programming (OOP) for Beginners
# ============================================================

# ============================================================
# 1. Defining a Class
# ============================================================
class Dog:
    # Class variable — shared by all instances
    species = "Canis lupus familiaris"

    # __init__ is the constructor — runs when object is created
    def __init__(self, name, age):
        self.name = name       # instance variable
        self.age = age

    # Instance method — first param is always self
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating objects (instances)
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

dog1.bark()                    # Rex says: Woof!
dog2.describe()                # Bella is 5 years old.
print(Dog.species)             # Canis lupus familiaris

# ============================================================
# 2. __str__ — human-readable string representation
# ============================================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(p)                       # Point(3, 4)  — uses __str__
print(repr(p))                 # Point(x=3, y=4) — uses __repr__

# ============================================================
# 3. Inheritance — child class reuses parent class
# ============================================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):             # Cat inherits from Animal
    def speak(self):           # override parent method
        print(f"{self.name} says: Meow!")

class Duck(Animal):
    def speak(self):
        print(f"{self.name} says: Quack!")

cat = Cat("Whiskers")
duck = Duck("Donald")

cat.speak()                    # Whiskers says: Meow!
duck.speak()                   # Donald says: Quack!

# isinstance() — check if object is an instance of a class
print(isinstance(cat, Cat))    # True
print(isinstance(cat, Animal)) # True (Cat inherits Animal)
print(isinstance(cat, Duck))   # False

# ============================================================
# 4. super() — call parent class method
# ============================================================
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand} — top speed: {self.speed} km/h")

class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)   # call Vehicle.__init__
        self.battery = battery

    def describe(self):
        super().describe()               # call Vehicle.describe
        print(f"Battery: {self.battery} kWh")

tesla = ElectricCar("Tesla", 250, 100)
tesla.describe()
# Tesla — top speed: 250 km/h
# Battery: 100 kWh

# ============================================================
# 5. Class methods and Static methods
# ============================================================
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):            # cls refers to the class
        return cls.count

    @staticmethod
    def description():             # no access to class or instance
        return "Counts how many instances were created."

Counter()
Counter()
Counter()
print(Counter.get_count())         # 3
print(Counter.description())       # Counts how many instances were created.

# ============================================================
# 6. Encapsulation — private attributes (convention: _single, __double)
# ============================================================
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # name-mangled — harder to access directly

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())       # 1300

# ============================================================
# Summary
# ============================================================
# Concept          | Keyword / Syntax
# -----------------+------------------------------------------
# Define class     | class MyClass:
# Constructor      | def __init__(self, ...):
# Instance method  | def method(self):
# Class variable   | declared outside __init__
# Instance variable| self.var = value inside __init__
# Inheritance      | class Child(Parent):
# Override method  | redefine method in child class
# Call parent      | super().method()
# Class method     | @classmethod  def fn(cls):
# Static method    | @staticmethod def fn():
# String repr      | __str__, __repr__
