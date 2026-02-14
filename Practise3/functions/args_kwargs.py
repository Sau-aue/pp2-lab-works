# 1
def sum_all(*args):
    return sum(args)

# 2
def multiply_all(*args):
    result = 1
    for x in args:
        result *= x
    return result

# 3
def print_all(*args):
    for item in args:
        print(item)

# 4
def find_max(*args):
    return max(args)

# 5
def count_args(*args):
    return len(args)
