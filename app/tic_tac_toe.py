def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
        print("-------------")


def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def get_row(player):
    while True:
        try:
            row = int(input(f"Игрок {player}, введите номер строки (1-3): ")) - 1
            if row < 0 or row > 2:
                print("Некорректный ввод. Пробуйте снова.")
                continue
            return row
        except ValueError:
            print("Некорректный ввод. Пробуйте снова.")


def get_col(player):
    while True:
        try:
            col = int(input(f"Игрок {player}, введите номер столбца (1-3): ")) - 1
            if col < 0 or col > 2:
                print("Некорректный ввод. Пробуйте снова.")
                continue
            return col
        except ValueError:
            print("Некорректный ввод. Пробуйте снова.")
