from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 1) map - квадраты чисел
squares = list(map(lambda x: x * x, numbers))
print("Example 1:", squares)


# 2) map - перевести числа в строки
strings = list(map(str, numbers))
print("Example 2:", strings)


# 3) filter - оставить только четные
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Example 3:", evens)


# 4) filter - оставить числа больше 2
greater_than_2 = list(filter(lambda x: x > 2, numbers))
print("Example 4:", greater_than_2)


# 5) reduce - найти произведение всех чисел
product = reduce(lambda a, b: a * b, numbers)
print("Example 5:", product)