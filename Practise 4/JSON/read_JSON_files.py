#1
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)

#2 to get info
print(data["name"])

#3
with open("students.json", "r") as f:
    students = json.load(f)

print(students[0]["name"])

#4 
for student in students:
    print(student["grade"])

#5
if "age" in data:
    print(data["age"])

    