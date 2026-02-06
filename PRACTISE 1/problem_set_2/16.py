n = int(input())
a = list(map(int, input().split()))

mp = {}

for x in a:
    if x in mp:
        print("NO")
    else:
        print("YES")
        mp[x] = 1
