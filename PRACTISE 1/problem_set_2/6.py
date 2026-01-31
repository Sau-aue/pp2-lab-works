
n = int(input())
digits = input().split()
max = int(digits[0])
for i in range(0,n,1):
    if max < int(digits[i]):
        max = int(digits[i])
print(max)