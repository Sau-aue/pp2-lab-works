# 1
class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class C(A, B):
    pass

c = C()
c.a()
c.b()

# 2
class Fly:
    def move(self):
        print("Flying")

class Swim:
    def move2(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

Duck().move()
Duck().move2()

# 3
class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def call(self):
        print("Calling...")

class Smartphone(Camera, Phone):
    pass

s = Smartphone()
s.take_photo()
s.call()

# 4
class USB:
    def connect(self):
        print("USB connected")

class Bluetooth:
    def connect_wireless(self):
        print("Bluetooth connected")

class Headphones(USB, Bluetooth):
    pass

h = Headphones()
h.connect()
h.connect_wireless()

# 5
class Writer:
    def write(self):
        print("Writing...")

class Reader:
    def read(self):
        print("Reading...")

class Student(Writer, Reader):
    pass

st = Student()
st.write()
st.read()
