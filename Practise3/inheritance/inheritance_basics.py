# 1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

Dog().speak()

# 2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Aman")
print(s.name)

# 3
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    pass

Car().move()

# 4
class Shape:
    def info(self):
        print("I am a shape")

class Circle(Shape):
    pass

Circle().info()

# 5
class Device:
    def turn_on(self):
        print("Device ON")

class Phone(Device):
    pass

Phone().turn_on()
