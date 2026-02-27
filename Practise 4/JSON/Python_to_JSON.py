#1 dict in JSON
import json

data = {"name": "Ali", "age": 20}
json_data = json.dumps(data)

print(json_data)

#2 list 
import json

nums = [1, 2, 3]
print(json.dumps(nums))

#3 indent
import json

data = {"name": "Ali", "age": 20}
print(json.dumps(data, indent=4))

#4 key filter
import json

data = {"b": 2, "a": 1}
print(json.dumps(data, sort_keys=True))

#5 complex structure
import json

data = {
    "students": [
        {"name": "Ali", "grade": 90},
        {"name": "Sara", "grade": 95}
    ]
}

print(json.dumps(data, indent=2))