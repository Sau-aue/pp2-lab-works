# 1
nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
print(squares)

# 2
nums = [1, 2, 3]
plus5 = list(map(lambda x: x + 5, nums))
print(plus5)

# 3
nums = [2, 4, 6]
halves = list(map(lambda x: x / 2, nums))
print(halves)

# 4
words = ["a", "bb", "ccc"]
lengths = list(map(lambda w: len(w), words))
print(lengths)

# 5
nums = [-1, -2, 3]
absolute = list(map(lambda x: abs(x), nums))
print(absolute)
