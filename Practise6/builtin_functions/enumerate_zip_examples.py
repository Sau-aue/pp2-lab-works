names = ["Ali", "Dana", "Mira"]
scores = [90, 85, 95]

# 1) enumerate - индексы и значения
print("Example 1:")
for i, name in enumerate(names):
    print(i, name)


# 2) enumerate с началом с 1
print("\nExample 2:")
for i, name in enumerate(names, start=1):
    print(i, name)


# 3) zip - склеить два списка
print("\nExample 3:")
for name, score in zip(names, scores):
    print(name, score)


# 4) Сделать словарь через zip
student_scores = dict(zip(names, scores))
print("\nExample 4:")
print(student_scores)


# 5) enumerate + zip вместе
print("\nExample 5:")
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} -> {score}")