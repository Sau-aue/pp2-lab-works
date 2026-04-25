def isUsual(num):
    for numbers in (2,3,5):
        while num % numbers == 0:
            num//=numbers
    if num == 1:
        return True
    else:
        return False
    

n = int(input())
truth = isUsual(n)
if truth == True:
    print("Yes")
else:
    print("No")