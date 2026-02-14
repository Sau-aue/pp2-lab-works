# 1
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 2
nums = [10, 15, 20, 25]
greater = list(filter(lambda x: x > 15, nums))
print(greater)

# 3
words = ["cat", "elephant", "dog"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)

# 4
nums = [-5, 3, -2, 8]
positives = list(filter(lambda x: x > 0, nums))
print(positives)

# 5
nums = [1, 3, 5, 7]
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd)
