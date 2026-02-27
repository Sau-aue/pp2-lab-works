#1 открыть и вывести всех
import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

for user in data["users"]:
    print(user["name"])

#2 найти пользователя старше 22
for user in data["users"]:
    if user["age"] > 22:
        print(user["name"])

#3 add new user
data["users"].append({"name": "John", "age": 30})

#4 save again to the file
with open("sample-data.json", "w") as f:
    json.dump(data, f, indent=2)

#5 count average age
ages = [user["age"] for user in data["users"]]
print(sum(ages) / len(ages))

