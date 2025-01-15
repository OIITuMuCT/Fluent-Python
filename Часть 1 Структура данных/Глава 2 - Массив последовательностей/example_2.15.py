# Пример 2.15. Список содержащий три ссылки на один и тот же список, бесполезен

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = "O"
print(weird_board)