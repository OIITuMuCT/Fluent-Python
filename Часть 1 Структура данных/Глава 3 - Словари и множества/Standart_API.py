# Стандартый API типов отображений
from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))

# Что значит хешируемый?
# Объект называется хешируемым, если имеет хеш-код,
# который не изменяется на протяжении всего времени
# его жизни(у него должен быть метод __hash__()), и
# допускает сравнение с другими объектами
# (у него должен быть метод __eq__()). Если в результате
# сравнения хешируемых объектов оказывается, что они равны,
# то и их хэш-коды должны быть равны.

tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, (30, 40))
print(hash(tl))
tf = (1,2, frozenset([30, 40]))
print(tt is tl)
print(tt == tl)
print(hash(tf))
tn = (1, 2, (30, 40))
print(hash(tn))

