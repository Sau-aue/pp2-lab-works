import re

text = "I have 2 apples and 10 bananas"

numbers = re.findall(r"\d+", text)

print(numbers)

#['2', '10'] output and \d+ it means here однф или больше букв 