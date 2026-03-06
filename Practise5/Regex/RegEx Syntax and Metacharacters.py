import re

# . which means any symbol
text = "cat cot cut"

print(re.findall("c.t", text))

# * and result ['go', 'goo', 'gooo']
text = "go goo gooo"

print(re.findall("go*", text))

#+ ['go', 'goo', 'gooo']
text = "go goo gooo"

print(re.findall("go+", text))

# result ['color', 'colour'] ?
text = "color colour"

print(re.findall("colou?r", text))

# ^ result ['hello']
text = "hello world"

print(re.findall("^hello", text))

#$ result ['python']
text = "I love python"

print(re.findall("python$", text))

# result ['cat','bat','rat'] []
text = "cat bat rat"

print(re.findall("[cbr]at", text))


#| result ['cat','dog']
text = "cat dog fish"

print(re.findall("cat|dog", text))

#[('John','25'), ('Mike','30')] ()
text = "John:25 Mike:30"

print(re.findall(r"(\w+):(\d+)", text))