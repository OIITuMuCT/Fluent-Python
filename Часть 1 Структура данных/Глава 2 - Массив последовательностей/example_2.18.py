# Пример 2.18. 

>>> dis.dis('s[a] += b')
1							0 LOAD_NAME         0 (s)
                            3 LOAD_NAME         1 (a)
                            6 DUP_TOP_TWO
                            7 BINARY_SUBSCR
                            8 LOAD_NAME         2 (b)
                            11 INPLACE_ADD
                            12 ROT_THREE
                            13 STORE_SUBSCR
                            14 LOAD_CONST       0 (None)
                            17 RETURN_VALUE




# 1 Поместить значение s[a] на вершину стека (TOS).
# 2 Выполнить TOS += b. Эта операция завершается успешно, если TOS ссылается
# на изменяемый объект (в примере 2.17 это список).
# 3 Выполнить присваивание s[a] = TOS. Эта операция завершается неудачно,
# если s – неизменяемый объект (в примере 2.17 это кортеж t).
