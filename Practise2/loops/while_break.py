# 1 example
num = 8
while num < 99:
  print(num)
  if num == 28:
    break
  num += 10

# 2 example 
age = input()
while age == ValueError:
  print("enter valid name")
  if age != ValueError:
    break

# 3 example 
num = int(input())
while num == ValueError:
  print("Enter numbers")
  if num != ValueError:
    if num % 2 != 0:
      print("enter even number")
    else:
      break

# 4 example 
ab = 55
while ab % 2 != 0:
  ab -= 1
  if ab % 2 == 0:
    break

# 5 example 
l = [1 , 3 , 4]
sum = 156
sum1 = 0
while sum > sum1:
  sum1 += l[0] + l[1] + l [2]
  if sum < sum1:
    break