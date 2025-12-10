square = lambda x: x * x

print(square(5))


def myfunc(n):
    return lambda y : y * n

mytripple = myfunc(3)

print(mytripple(4))