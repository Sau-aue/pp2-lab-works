n = int(input())
a = input().split()

mx = int(a[0])
pos = 0

for i in range(0,n,1):
    if mx < int(a[i]):
        mx = int(a[i])
        pos = i

print(pos+1)
