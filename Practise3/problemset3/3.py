s = input()


to_digit = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}


to_word = {v: k for k, v in to_digit.items()}


if "+" in s:
    left, right = s.split("+")
    op = "+"
elif "-" in s:
    left, right = s.split("-")
    op = "-"
else:
    left, right = s.split("*")
    op = "*"


def decode(x):
    number = ""
    for i in range(0, len(x), 3):
        part = x[i:i+3]
        number += to_digit[part]
    return int(number)

a = decode(left)
b = decode(right)


if op == "+":
    result = a + b
elif op == "-":
    result = a - b
else:
    result = a * b


answer = ""
for digit in str(result):
    answer += to_word[digit]

print(answer)
