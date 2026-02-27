#1 simple counter
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

c = Counter(3)

for x in c:
    print(x)

#2 even numbers
class Even:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        return self.num
    
#3 even numbers but until 10
class Even:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num > 10:
            raise StopIteration
        return self.num
    
#4 reversed counter
class Down:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        self.num -= 1
        return self.num
    
#5
class Letters:
    def __init__(self):
        self.ch = ord('A')

    def __iter__(self):
        return self

    def __next__(self):
        if self.ch > ord('C'):
            raise StopIteration
        letter = chr(self.ch)
        self.ch += 1
        return letter