# Кортежи как неизменяемые списки
a = (10, "alpha", [1, 2])
b = (10, "alpha", [1, 2])
print(a == b)
b[-1].append(99)
print(a == b)

print(a)
print(b)

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, "alpha", (1, 2))
tm = (10, "alpha", [1, 2])
print(fixed(tf))
print(fixed(tm))

#  Распаковка последовательностей и итерируемых объектов
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

b, a = a, b

# Использование * для выборки лишних элементов
a, b, *rest = range(5)
print(a, b, rest)

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


print(fun(*[1, 2], 3, *range(4, 7)))

print("*range(5), 4 = ", *range(4), 4)
print("[*range(10), 10] = ", [*range(10), 11])
print("{*range(4), 4, *(4, 5, 6)} = ", x := {*range(4), 4, *(4, 5, 6)}, type(x))


