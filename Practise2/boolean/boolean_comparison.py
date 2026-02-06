#1 example comparison boolean will return True or False about th condition
x = 159
y = 78942

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# 2 example Python allows to chain comparison operators:
ao = 89
if 0 < ao < 100:
    print("Yes")
print(15 < ao < 90)

#3 example 

p = 78999 
op = 10
print(p != op) #not equals to also returns boolean
if p <= op: # bigger/smaller or equal to 
    print("Yes")

# 4 example 
print(5 == 5)
boolean_name = True
number = 159
if boolean_name and number > 100:
    print("Yes")

# 5 example 
numberss = 4569787
if numberss**2 != 78945646123:
    print("True")