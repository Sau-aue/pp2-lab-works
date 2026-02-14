# 1
class Animal:
    def speak(self):
        print("...")

class Cat(Animal):
    def speak(self):
        print("Meow")

Cat().speak()

# 2
class Vehicle:
    def move(self):
        print("Moving")

class Bike(Vehicle):
    def move(self):
        print("Pedaling")

Bike().move()

# 3
class Employee:
    def salary(self):
        return 1000

class Manager(Employee):
    def salary(self):
        return 1500

print(Manager().salary())

# 4
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a

print(Square(4).area())

# 5
class Printer:
    def print_text(self):
        print("Printing...")

class LaserPrinter(Printer):
    def print_text(self):
        print("Laser printing...")

LaserPrinter().print_text()
