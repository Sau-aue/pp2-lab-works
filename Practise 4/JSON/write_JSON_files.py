#1 write in file
import json

data = {"name": "Ali", "age": 20}

with open("data.json", "w") as f:
    json.dump(data, f)

#2 beautyfully write it
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

#3 
import json

nums = [1, 2, 3]

with open("nums.json", "w") as f:
    json.dump(nums, f)

#4 
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Sara", "grade": 95}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

#5
import json

data = {"new_key": 123}

with open("data.json", "w") as f:
    json.dump(data, f)