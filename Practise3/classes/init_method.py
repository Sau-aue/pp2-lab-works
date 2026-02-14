# 1
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Aman")
print(s.name)

# 2
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

c = Car("BMW", 200)
print(c.brand, c.speed)

# 3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x, p.y)

# 4
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

acc = BankAccount(1000)
print(acc.balance)

# 5
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b = Book("Python", 300)
print(b.title, b.pages)
