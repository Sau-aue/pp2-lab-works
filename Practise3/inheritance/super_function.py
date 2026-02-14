# 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

s = Student("Aman", 3.5)
print(s.name, s.gpa)

# 2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

Dog().speak()

# 3
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

c = Car(200, "BMW")
print(c.speed, c.brand)

# 4
class Employee:
    def total_salary(self):
        return 1000

class Manager(Employee):
    def total_salary(self):
        return super().total_salary() + 500

print(Manager().total_salary())

# 5
class Base:
    def show(self):
        print("Base show")

class Child(Base):
    def show(self):
        super().show()
        print("Child show")

Child().show()
