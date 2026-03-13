# 1) Записать текст в новый файл
with open("write1.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!")

print("Example 1 done")


# 2) Записать несколько строк
with open("write2.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

print("Example 2 done")


# 3) append - добавить новую строку
with open("write3.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")

with open("write3.txt", "a", encoding="utf-8") as f:
    f.write("Second line\n")

print("Example 3 done")


# 4) writelines() - записать список строк
lines = ["Python\n", "C++\n", "Java\n"]
with open("write4.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Example 4 done")


# 5) Проверить содержимое после append
with open("write5.txt", "w", encoding="utf-8") as f:
    f.write("Start\n")

with open("write5.txt", "a", encoding="utf-8") as f:
    f.write("Middle\n")
    f.write("End\n")

with open("write5.txt", "r", encoding="utf-8") as f:
    print("Example 5:")
    print(f.read())