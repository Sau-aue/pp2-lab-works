n = int(input())
isPrime = True
for i in range(2, n , 1):
    if n % i == 0:
        isPrime = False
if isPrime == False:
    print("No")
else:
    print("Yes")