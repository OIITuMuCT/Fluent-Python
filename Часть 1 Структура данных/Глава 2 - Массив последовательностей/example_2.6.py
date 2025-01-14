# Пример 2.6. Порождение декартова произведения генераторным выражением

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# 1 генераторное выражение отдает по одному элементу за раз;
# список, содержащий шесть вариаций футболки, не создается.
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
