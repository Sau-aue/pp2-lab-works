def validnumber(number):
    isvalid = True
    for i in range(len(number)):
        if int(number[i]) % 2 == 1:
            return False
    return isvalid

n = input()
truth = validnumber(n)
if truth == True:
    print("Valid")
else:
    print("Not valid")

