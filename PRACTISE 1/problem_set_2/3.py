count = int(input())
seq = input().split()

m = []
for i in range(0, len(seq), 1):
    m.append(int(seq[i]))

total = 0
for x in m:
    total += x

print(total)
