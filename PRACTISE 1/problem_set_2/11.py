o = input().split()
n = int(o[0])
l = int(o[1])
r = int(o[2])

str1 = input()
num = str1.split()
for i in range(len(num)):
    num[i] = int(num[i])
num[l-1:r] = num[l-1:r][::-1]
print(*num)


