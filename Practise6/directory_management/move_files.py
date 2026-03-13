import shutil
import os

# Подготовка
os.makedirs("source_dir", exist_ok=True)
os.makedirs("target_dir", exist_ok=True)

# 1) Переместить файл
with open("source_dir/file1.txt", "w", encoding="utf-8") as f:
    f.write("Move me")

shutil.move("source_dir/file1.txt", "target_dir/file1.txt")
print("Example 1: file moved")


# 2) Скопировать файл в другую папку
with open("source_dir/file2.txt", "w", encoding="utf-8") as f:
    f.write("Copy me")

shutil.copy("source_dir/file2.txt", "target_dir/file2_copy.txt")
print("Example 2: file copied")


# 3) Переименовать файл через move
with open("source_dir/file3.txt", "w", encoding="utf-8") as f:
    f.write("Rename me")

shutil.move("source_dir/file3.txt", "source_dir/renamed_file3.txt")
print("Example 3: file renamed")


# 4) Найти все .txt файлы в папке
print("Example 4:")
for name in os.listdir("source_dir"):
    if name.endswith(".txt"):
        print(name)


# 5) Переместить все .txt файлы из source_dir в target_dir
for name in os.listdir("source_dir"):
    if name.endswith(".txt"):
        shutil.move(os.path.join("source_dir", name), os.path.join("target_dir", name))

print("Example 5: all txt files moved")