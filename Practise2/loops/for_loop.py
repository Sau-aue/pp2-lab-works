#1 example print each thing in list
name = ["U", "Yuki","Nu"]
for x in name:
  print(x)

# 2 example Looping Through a String
s = "United Nations"
for c in s:
  print(c)

# 3 example range() starts 0 by deafult end is always not included
for x in range(2, 6):
  print(x)

# 4 example 

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# 5 example 
word = "Margarita but i how to spell m?"
cnt = 0

for letter in word:
    if letter == "m":
        cnt += 1

print("m:", cnt)



