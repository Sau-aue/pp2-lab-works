import re
#\d
text = "abc123"
print(re.findall(r"\d", text))
# result ['1','2','3']


#\w
text = "hello_123"

print(re.findall(r"\w", text))


#\s
text = "hello world"

print(re.findall(r"\s", text))

#\D
text = "abc123"

print(re.findall(r"\D", text))
#result ['a','b','c']

#\W
text = "hello@123"

print(re.findall(r"\W", text))
#result ['@']


#\S
text = "a b c"

print(re.findall(r"\S", text))
#result ['a','b','c']