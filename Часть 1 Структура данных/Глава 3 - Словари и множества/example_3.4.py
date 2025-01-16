# Пример 3.4. index0.py: применение метода dict.get для выборки и обновления списка
# вхождений слова в индекс (в примере 3.4 показано лучшее решение)
""" Строим индекс, отображающий слово на список его вхождений """
import re
import sys

WORD_RE = re.compile(r'\w+')
index = dict(api=1, author="Douglas Hofstadter", type="book", title="Gödel, Escher, Bach")
index = {}
with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # некрасиво; написано только для демонстрации идеи
            occurrences = index.get(word, []) # 1
            occurrences.append(location)   # 2
            index[word] = occurrences # 3
# Напечатать в алфавитном порядке
for word in sorted(index, key=str.upper): # 4
    print(word, index[word])

# 1 Получить список вхождений слова word или [], если оно не найдено.
# 2 Добавить новое вхождение в occurrences.
# 3 Поместить модифицированный список occurrences в словарь dict; при этом
# производится второй поиск в индексе.
# 4 При задании аргумента key функции sorted мы не вызываем str.upper, а толь-
# ко передаем ссылку на этот метод, чтобы sorted могла нормализовать слова
# перед сортировкой
