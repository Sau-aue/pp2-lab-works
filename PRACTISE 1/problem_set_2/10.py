o = int(input())
n = input()
a = n.split()
l = []
for i in range(o):
    l.append(int(a[i]))
l.sort()
d = list(reversed(l))
print(*d)
