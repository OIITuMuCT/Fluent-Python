# Пример 2.1. Построить список кодовых позиций Unicode по строке

symbols = "$¢£¥€¤"

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)