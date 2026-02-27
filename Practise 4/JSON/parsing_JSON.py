#1
import json

data = '{"name": "Ali", "age": 20}'
parsed = json.loads(data)

print(parsed["name"])

#2 list
import json

data = '[1, 2, 3]'
nums = json.loads(data)

print(nums[0])

#3 nested info
import json

data = '{"student": {"name": "Sara", "grade": 95}}'
parsed = json.loads(data)

print(parsed["student"]["grade"])

#4 true -> True
import json

data = '{"active": true}'
parsed = json.loads(data)

print(parsed["active"])

#5 null -> None
import json

data = '{"value": null}'
parsed = json.loads(data)

print(parsed["value"])