# Write your code below this line 👇


def add(*args):
    l = len(args)
    sum = 0
    i = 0
    while (i < l):
        sum += args[i]
        i = i + 1
    return sum


print("total:", add(2, 3, 4, 5))
