#1
def gen():
    yield 1
    yield 2
    yield 3

for x in gen():
    print(x)

#2
def count(n):
    for i in range(n):
        yield i

for x in count(5):
    print(x)

#3
def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

#4
def letters():
    yield "A"
    yield "B"

#5 infinite generator
def infinite():
    num = 1
    while True:
        yield num
        num += 1