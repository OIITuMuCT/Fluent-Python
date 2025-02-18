# Пример 2.23. Работа с очередью

from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

# 1 Необязательный аргумент maxlen задает максимальное число элементов
# в этом экземпляре deque, при этом устанавливается допускающий только
# чтение атрибут экземпляра maxlen.
# 2 В результате циклического сдвига с n > 0 элементы удаляются с правого
# конца и добавляются с левого; при n < 0 удаление производится с левого
# конца, а добавление – с правого.
# 3 При добавлении элемента в заполненную очередь (len(d) == d.maxlen) про-
# исходит удаление с другого конца; обратите внимание, что в следующей
# строке элемент 0 отсутствует.
# 4 При добавлении трех элементов справа удаляются три элемента слева: –1,
# 1 и 2.
# 5 Отметим, что функция extendleft(iter) добавляет последовательные эле-
# менты из объекта iter в левый конец очереди, т. е. в итоге элементы будут
# размещены в порядке, противоположном исходному.