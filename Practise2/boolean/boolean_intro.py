# 1 example
print(10 > 9)
print(10 == 9)
print(10 < 9) #comparing 2 values (returns False or True)

#2 example 
# evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15)) #returns True

#3 example Evaluate two values
x = "Banana"
y = 10000

print(bool(x))
print(bool(y))

#4 example Most values are true except empty strings, 0 in integer, list set tuple dict that empty
bool("abcedftrh")
bool(5678)
bool(["apple", "cherry", "banana"]) #all of them will return True as they not empty

#5 example 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) # this will return False as they empty
