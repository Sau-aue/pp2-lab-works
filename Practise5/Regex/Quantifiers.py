import re

#{n}
text = "111 11 1"

print(re.findall(r"\d{3}", text))
# result ['111']

#{n,}
text = "111 11 1"

print(re.findall(r"\d{2,}", text))
#result ['111','11']


#{n,m}
text = "1 12 123 1234"

print(re.findall(r"\d{2,3}", text))
#result ['12','123']


"""re.search()

Ищет первое совпадение.
"""
text = "My number is 12345"

match = re.search(r"\d+", text)

print(match.group())
#result 12345


"""re.findall()

Ищет все совпадения.
"""
text = "1 22 333"

print(re.findall(r"\d+", text))
#result ['1','22','333']


"""re.split()

Разделяет строку.
"""
text = "apple,banana;orange"

result = re.split("[,;]", text)

print(result)
#result ['apple','banana','orange']


"""re.sub()

Заменяет текст.
"""
text = "Price: 100 dollars"

result = re.sub(r"\d+", "XXX", text)

print(result)
#output Price: XXX dollars


"""re.match()

Проверяет начало строки.
"""
text = "hello world"

print(re.match("hello", text))

#Если совпало -> вернет объект.


#Flags


"""re.IGNORECASE

Игнорирует регистр.
"""
text = "Hello hello"

print(re.findall("hello", text, re.IGNORECASE))
#output ['Hello','hello']


"""re.MULTILINE

Позволяет ^ работать на каждой строке.
"""
text = """cat
dog
fish"""

print(re.findall("^dog", text, re.MULTILINE))