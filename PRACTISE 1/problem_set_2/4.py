n = int(input())
cnt = 0
a = input().split()
for i in range(0,len(a),1):
    if int(a[i]) > 0:
        cnt+=1
print(cnt)

