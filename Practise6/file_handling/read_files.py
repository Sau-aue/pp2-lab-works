# 1) read() - прочитать весь файл целиком
with open("sample1.txt", "w", encoding="utf-8") as f:
    f.write("Hello\nWorld\nPython")

with open("sample1.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Example 1:")
    print(content)


# 2) readline() - прочитать первую строку
with open("sample2.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine 2\nLine 3")

with open("sample2.txt", "r", encoding="utf-8") as f:
    print("\nExample 2:")
    print(f.readline().strip())


# 3) readlines() - получить список строк
with open("sample3.txt", "w", encoding="utf-8") as f:
    f.write("Apple\nBanana\nCherry")

with open("sample3.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("\nExample 3:")
    print(lines)


# 4) Чтение файла построчно через for
with open("sample4.txt", "w", encoding="utf-8") as f:
    f.write("A\nB\nC")

print("\nExample 4:")
with open("sample4.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# 5) Подсчет количества строк в файле
with open("sample5.txt", "w", encoding="utf-8") as f:
    f.write("One\nTwo\nThree\nFour")

with open("sample5.txt", "r", encoding="utf-8") as f:
    line_count = len(f.readlines())
    print("\nExample 5:")
    print("Lines:", line_count)