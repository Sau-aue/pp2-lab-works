digit = int(input())

n = 0
while n < 99:
    number = 2 << n
    if number == digit:
        print("YES")
        exit()
    n+=1
print("NO")