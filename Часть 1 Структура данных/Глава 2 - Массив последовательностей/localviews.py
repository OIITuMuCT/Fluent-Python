# Локальная область видимости внутри включений и генераторных выражений

x = 'ABC'

codes = [ord(x) for x in x]
print(x) # #1 Значение х не перезаписано: оно по-прежнему привязано к 'ABC'.
print(codes)
codes = [last := ord(c) for c in x]
print(last) # #2 last осталось таким же, как прежде

c # c пропала, она существовала только внутри listcomp
print(c)
