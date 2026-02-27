#1 square of digit
def squares(n):
    for i in range(n):
        yield i * i

#2 fibonacci
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

#3 filter
def positive(nums):
    for n in nums:
        if n > 0:
            yield n

#4 
def chars(s):
    for ch in s:
        yield ch

#5
def reverse(lst):
    for i in range(len(lst)-1, -1, -1):
        yield lst[i]