# Пример 3.2. creator.py: ger_creators() выделяет имена авторов из записей о произведениях

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'author':[*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name }:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record:{record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        
# 1(case) Сопоставить с любым отображением, в котором 'type': 'book', 'api' : 2, а ключу 'authors' соответствует последовательность. Вернуть элементы последова-
# тельности в виде нового списка.
# 2 Сопоставить с любым отображением, в котором 'type': 'book', 'api' : 1, а клю-
# чу 'author' соответствует произвольный объект. Вернуть этот объект в виде
# элемента списка.
# 3 Любое другое отображение, в котором 'type': 'book', недопустимо, возбу-
# дить исключение ValueError.
# 4 Сопоставить с любым отображением, в котором 'type': 'movie', а ключу
# 'director' соответствует одиночный объект. Вернуть этот объект в виде эле-
# мента списка.
# 5 Любой другой субъект недопустим, возбудить исключение ValueError.