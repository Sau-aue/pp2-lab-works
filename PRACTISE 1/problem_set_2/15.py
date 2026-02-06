n = int(input())
mp = {}
for i in range(n):
    s = input()
    mp[s] = mp.get(s , 0) + 1

print(len(mp))