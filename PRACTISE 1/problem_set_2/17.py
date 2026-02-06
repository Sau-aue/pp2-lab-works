n = int(input())
mp = {}

for i in range(n):
    phone = input().strip()
    mp[phone] = mp.get(phone, 0) + 1

cnt = 0
for phone in mp:
    if mp[phone] == 3:
        cnt += 1

print(cnt)
