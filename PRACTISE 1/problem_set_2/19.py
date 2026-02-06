n = int(input())
mp = {}

for _ in range(n):
    name, k = input().split()
    k = int(k)
    mp[name] = mp.get(name, 0) + k

for name in sorted(mp):
    print(name, mp[name])
