# Пример 2.14. Список, содержащий три списка длины 3, 
# может представлять поле для игры в крестики нолики

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)