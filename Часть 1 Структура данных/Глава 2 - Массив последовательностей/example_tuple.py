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
