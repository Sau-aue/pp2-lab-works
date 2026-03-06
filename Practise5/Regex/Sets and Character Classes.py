import re
text = "apple banana cherry"

print(re.findall("[aeiou]", text))

#Найдет все гласные.

re.findall("[a-z]", text)
#все маленькие буквы

