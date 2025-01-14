# Пример 2.2. Построить список кодовых позиций Unicode по строке с применением listcomp 

symbols = "$¢£¥€¤"

codes = [ord(symbol) for symbol in symbols]
print(codes)
