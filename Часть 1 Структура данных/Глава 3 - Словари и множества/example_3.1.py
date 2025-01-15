# Пример 3.1. Примеры словарных включений
dial_codes = [ 
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States"),
]
country_dial = {country: code for code, country in dial_codes}
print(country_dial)
print({code: country.upper() for country, code in country_dial.items() if code < 70})
# 1 Итерируемый объект dial_codes, содержащий список пар ключ-значение,
# можно напрямую передать конструктору dict, но…
# 2 … мы инвертируем пары: ключом является country, а значением – code.
# 3 Сортируем country_dial по названию страны, снова инвертируем пары, пре-
# образуем значения в верхний регистр и оставляем только элементы, для
# которых code < 70.