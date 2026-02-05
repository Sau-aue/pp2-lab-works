n = int(input())
a = list(map(int, input().split()))

cnt = {}
for x in a:
    cnt[x] = cnt.get(x, 0) + 1

mx = max(cnt.values())

best = None
for x in cnt:
    if cnt[x] == mx:
        if best is None or x < best:
            best = x

print(best)
