a = int(input())
n = 0
isFinish= False

while isFinish == False:
    if 2 ** n <= a:
        print(2 ** n, end=" ")
        n+=1
        
    else:
        break

