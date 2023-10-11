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


def play_again():
    while True:
        answer = input("Do you want to play again? (yes or no): ")
        if answer.lower() == "yes":
            return True
        elif answer.lower() == "no":
            return False
        else:
            print("Invalid input. Try again.")


def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        row = get_row(players[current_player])
        col = get_col(players[current_player])
        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue
        board[row][col] = players[current_player]
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        if all(" " not in row for row in board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = (current_player + 1) % 2
    if play_again():
        play_game()