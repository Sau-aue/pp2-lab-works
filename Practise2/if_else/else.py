#1 example 
x = 15
y = 33
if y > x:
  print("y is greater than x")
elif x == y:
  print("x and y are equal")
else:
  print("x is greater than y")

# 2 example 
name = "Nurs"
if len(name) == 5:
  print("Yes")
else:
  print(name)

# 3 example

digit = 18

if digit % 2 == 0:
  print("Number is even")
else:
  print("Number is odd")

# 4 example 
import random
n = random.randint(1, 100)
if n < 18:
  print("you win")
elif 18 < n < 27:
  print("partially win")
else:
  print("you lose")

# 5 example else for error handling, validation, and providing default values
name = input()
if len(name) == 4:
  print(f"you have amazing name, {name}")
else:
  print("Error: your name is too long")
