import shutil
import os

# 1) Создать файл и скопировать его
with open("original1.txt", "w", encoding="utf-8") as f:
    f.write("This is the original file.")

shutil.copy("original1.txt", "copy1.txt")
print("Example 1: file copied")


# 2) Создать backup-копию
with open("original2.txt", "w", encoding="utf-8") as f:
    f.write("Important data")

shutil.copy("original2.txt", "original2_backup.txt")
print("Example 2: backup created")


# 3) copy2() - копирует и метаданные тоже
with open("original3.txt", "w", encoding="utf-8") as f:
    f.write("Metadata copy example")

shutil.copy2("original3.txt", "copy3.txt")
print("Example 3: copy2 used")


# 4) Безопасное удаление файла
with open("temp_delete.txt", "w", encoding="utf-8") as f:
    f.write("Delete me")

if os.path.exists("temp_delete.txt"):
    os.remove("temp_delete.txt")
    print("Example 4: file deleted")


# 5) Проверка, существует ли файл перед удалением
filename = "not_existing.txt"

if os.path.exists(filename):
    os.remove(filename)
    print("Example 5: file deleted")
else:
    print("Example 5: file does not exist")