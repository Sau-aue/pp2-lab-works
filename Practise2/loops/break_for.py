# 1 example
char = ['1', 'n' , '28' , '%']
for x in char:
  print(x)
  if x == 'n':
    break
  
# 2 example 
s = ["o", "oppp", "name", "surname"]
for x in s:
  print(x)
  if x == 'oppp':
    break
  print(x)

# 3 example 

att = ["Nu", "M" , "MMM" , "Op"]
for i in range(len(att)):
   if "M" == att[i]:
    break


# 4 example
password = "Letmein"

for i in range(0,5):
  guess = input()
  if guess == password:
    break
  elif guess != password:
    print("You have several attempts left")

# 5 example
import random
n = random.randint(1,100)
for i in range(5):
  m = int(input())
  if m == n:
    print("Yey you win")
    break
  else:
    print("Still have a chance")

    
