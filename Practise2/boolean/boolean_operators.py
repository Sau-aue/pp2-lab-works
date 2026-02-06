# 1 and or not logical operators
a = 15
b = 19
if a > 16 and b < 20:
    print("True") 
if a > 10 or b <20:
    print("True")
if not(a > 16 and b < 20):
    print("Why?")

# 2 example Identity Operators
x = ["Country", "Name"]
y = ["USA", "banana"]
z = y

print(x is z)
print(x is y)
print(x == y)

# 3 example 
x = ["Spain", "Canada"]
y = ["apple", "banana"]

print(x is not y)

# 4 example is - Checks if both variables point to the same object in memory but == - Checks if the values of both variables are equal
x = [15, 16 , 19]
y = [15, 16 , 19]

print(x == y)
print(x is y)

# 5 example Membership operator
countries = ["USA" , "Kazakhstan" , "Russia", "Spain"]

print("Uzbekstan" in countries)

print("Italy" not in countries)

# membership in strings
s = "Hello World"

print("ello" in s)
print("hello" in s)
print("Op" not in s)
