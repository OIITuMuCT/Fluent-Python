# Пример 2.12. Сопоставление с образцом с применением match/case

def evaluate(exp: Expression, env: Environment) -> Any:
"Evaluate an expression in an environment."
match exp:
# ... несколько строк опущено
    case ['quote', x]: # 1
        return x
    case ['if', test, consequence, alternative]: # 2
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    case ['lambda', [*parms], *body] if body: # 3
        return Procedure(parms, body, env)
    case ['define', Symbol() as name, value_exp]: # 4
        env[name] = evaluate(value_exp, env)
        # ... еще несколько строк опущено
    case _: # 5
        raise SyntaxError(lispstr(exp))


# 1Сопоставляется, если субъект – двухэлементная последовательность, 
# начинающаяся с 'quote'.
# 2 Сопоставляется, если субъект – четырехэлементная последовательность,
# начинающаяся с 'if'.
# 3 Сопоставляется, если субъект – последовательность из трех или более 
# элементов, начинающаяся с 'lambda'. Охранное условие гарантирует, что body не пусто.
# 4 Сопоставляется, если субъект – трехэлементная последовательность, 
# начинающаяся с 'define'.
# 5 Рекомендуется всегда включать перехватывающую ветвь case. В данном
# случае если exp не сопоставляется ни с одним образцом, значит, выражение
# построено неправильно, и я возбуждаю исключение SyntaxError.
