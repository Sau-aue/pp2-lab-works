#1
gen = (x*x for x in range(5))

for x in gen:
    print(x)

#2
gen = (x for x in range(10) if x % 2 == 0)

#3
nums = [1, 2, 3]
gen = (x+1 for x in nums)

#4
gen = (ch.upper() for ch in "hello")

#5
print(sum(x*x for x in range(5)))