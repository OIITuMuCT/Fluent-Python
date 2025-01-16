# Пример 3.5. index.py: применение метода dict.setdefault для выборки и обновления
# списка вхождений слова в индекс; в отличие от примера 3.4, понадобилась только одна
# строчка
"""Строит индекс, отображающий слово на список его вхождений"""
import re
import sys
WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# напечатать в алфавитном порядке
for word in sorted(index, key=str.upper):
    print(word, index[word])

# иными словами строка
# my_dict.setdefault(key, []).append(new_value)

# Дает такой же результат, как...

# if key not in my_dict:
#     my_dict[key] = []
# my_dict[key].append(new_value)
