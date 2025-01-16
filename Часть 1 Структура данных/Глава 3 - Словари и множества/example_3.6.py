# Пример 3.5. index_default.py: использование экземпляра defaultdict вместо метода
# setdefault

""" Строит индекс, отображающий слово на список его вхождений """

import collections
import re
import sys
WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list) # 1
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location) 
# напечатать в алфавитном порядке
for word in sorted(index, key=str.upper):
    print(word, index[word])

# 1 Создать defaultdict, задав в качестве default_factory конструктор list.

# 2 Если слова word еще нет в index, то вызывается функция default_factory, которая порождает отсутствующее значение – в данном случае пустой список.
# Это значение присваивается index[word] и возвращается, так что операция
# .append(location) всегда завершается успешно.
