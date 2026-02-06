# 1 example
strings = ["names" , "opinion" , "chance"]

for x in strings:
    if x == "names":
        continue
    print(x)

# 2 example 
names = ["Diana", "Aruzhan" , "Ali" ,"Alibek" ,"Beka"]

for x in names:
    if len(x) < 4:
        continue
    print(x)

# 3 example 
scores = [0 , 15 , 99 , 4567 , 990 , 0, 10 , 0]
sum = 0
cnt = 0
for x in scores:
    if x != 0:
        sum += x
        cnt += 1
    else:
        continue

print(sum/cnt)

# 4 example
password = "pa489w09rd"
allowed_for_use = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for char in password:
    if char in allowed_for_use:
        continue
    print("Forbidden symbol found:", char)

# 5 example
days = ["Monday" , "Tuesday" , "Wednesday", "Thursday","Friday" , "Saturday" ,"Sunday"]

for day in days:
    if day == "Sunday" or day == "Saturday":
        continue
    else:
        print(f"Working day:{day}")
        