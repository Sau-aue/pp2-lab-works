import os

# 1) Создать одну папку
os.mkdir("folder1")
print("Example 1: folder1 created")


# 2) Создать вложенные папки
os.makedirs("parent/child/grandchild")
print("Example 2: nested folders created")


# 3) Показать текущую директорию
print("Example 3:")
print(os.getcwd())


# 4) Показать содержимое текущей папки
print("Example 4:")
print(os.listdir("."))


# 5) Удалить пустую папку
os.mkdir("empty_folder")
os.rmdir("empty_folder")
print("Example 5: empty_folder removed")