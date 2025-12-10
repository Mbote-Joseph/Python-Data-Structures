square = lambda x: x * x

print(square(5))


def myfunc(n):
    return lambda y : y * n

mytripple = myfunc(3)

print(mytripple(4))

fruits = ["banana", "apple", "mango","coconut"]

title_fruit = list(map(lambda x: x.title(), fruits))
print(title_fruit)

print(map(fruits))