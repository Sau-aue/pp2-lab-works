# 1
nums = [5, 1, 4, 2]
print(sorted(nums))

# 2 (по длине строки)
words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda w: len(w)))

# 3 (по последней букве)
words = ["cat", "dog", "elephant"]
print(sorted(words, key=lambda w: w[-1]))

# 4 (по модулю числа)
nums = [-10, 5, -3, 2]
print(sorted(nums, key=lambda x: abs(x)))

# 5 (по второму элементу кортежа)
pairs = [(1, 5), (2, 3), (4, 1)]
print(sorted(pairs, key=lambda x: x[1]))
