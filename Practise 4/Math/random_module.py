#1
import random
print(random.random())   # число от 0 до 1

#2
import random
print(random.randint(1, 10))

#3
import random
colors = ["red", "blue", "green"]
print(random.choice(colors))

#4
import random
nums = [1, 2, 3, 4]
random.shuffle(nums)
print(nums)

#5
import random

secret = random.randint(1, 5)
guess = int(input("Guess number 1-5: "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong, number was", secret)