n = int(input())
mp = {}

for i in range(1, n + 1):   
    s = input()
    if s not in mp:
        mp[s] = i

for s in sorted(mp):
    print(s, mp[s])
