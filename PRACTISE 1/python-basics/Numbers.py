# 1 example int and float
money = 12345
pi = 3.14

#2 example complex numbers
x = 1+2j #used for imaginery numbers
print(x)
"""
!! we cannot use type conversion for complex numbers to make another variable in int or float
"""

# 3 example type conversion
a = 1
b = 15.06

c = complex(a)
d = int(b)
print(c) ; print(d)

# 4 example random numbers
import random
print(random.randrange(1,100))

# 5 example int is numbers without decimal point with unlimited length and can be both positivie and negative
number = -1245648978456545
print(number)
negative = -1234568
print(number + negative)