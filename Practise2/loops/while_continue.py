# 1 example
a = 25
while a < 100:
  a += 9
  if a == 99:
    continue
  print(a)

# 2 example 
age = 18
while age < 50:
  age /= 2
  age +=25
  if age == 34:
    continue

# 3 example
numbers = [15, 25 , 34]
sum = 0
while sum < 100:
  sum += numbers[0]+ numbers[1] + numbers[2]
  if sum > 70:
    continue
  
# 4 example
word = ""

while word != "python123":
    word = input("Enter word: ")
    if word == "":
        print("You entered nothing!")
        continue
    print("Wrong word!")    
print("Access given!")

# 5 example 
total = 0

while True:
    x = int(input("Enter a number (0 to stop): "))
    if x == 0:
        break
    if x < 0:
        continue
    total += x
print("Sum of positive numbers:", total)

