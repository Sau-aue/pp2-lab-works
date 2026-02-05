n = int(input())
seq = input().split()

for i in range(len(seq)):
    seq[i] = int(seq[i])

for i in range(len(seq)):
    seq[i] = seq[i]*seq[i]
print(*seq)