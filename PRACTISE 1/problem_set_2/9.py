n = int(input())
a = input().split()
mn = int(a[0])
mx = int(a[0])

for i in range(0, n ,1):
    if mn > int(a[i]):
        mn = int(a[i])
    elif mx < int(a[i]):
        mx = int(a[i])

for i in range(0, n ,1):
    if mx == int(a[i]):
        a[i] = str(mn)

for i in range(0, n ,1):
    print(a[i], end=" ")

        