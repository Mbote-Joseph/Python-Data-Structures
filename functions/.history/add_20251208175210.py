def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(add_all(1,2,3,4,5))