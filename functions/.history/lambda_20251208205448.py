square = lambda x: x * x

print(square(5))


def myfunc(n):
    return lambda y : y * n

mytripple = myfunc(3)

print(mytripple(4))

fruits = ["banana", "apple", "mango","coconut"]

title_fruit = list(map(lambda x: x.title(), fruits))
print(title_fruit)

fruit_a = list(filter(lambda a : a.startswith("a"), fruits))
print(fruit_a)


fruit_b = list(filter(lambda a : a.find("n"), fruits))
print(fruit_b)


numbers = [1,2,3,4,5,6,7,8,9]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
