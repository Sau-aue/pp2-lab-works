#1
nums = [10, 20, 30]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

#2
s = "ABC"
it = iter(s)

print(next(it))
print(next(it))

#3
nums = [1]
it = iter(nums)

print(next(it))
print(next(it))   # ошибка

#4
nums = [1]
it = iter(nums)

try:
    print(next(it))
    print(next(it))
except StopIteration:
    print("End")

#5
nums = [5, 6, 7]
it = iter(nums)

while True:
    try:
        print(next(it))
    except StopIteration:
        break