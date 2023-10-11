from behave import given, when, then

from app.tic_tac_toe import check_win


@given('Пустое игровое поле')
def step_given_empty_game_board(context):
    context.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

@when('Игрок выполнил условие выигрыша')
def step_when_player_completes_winning_condition(context):
    context.board = [["X", "O", "O"], ["O", "X", "O"], [" ", " ", "X"]]
    context.player = "X"

@then('Игра должна объявить игрока победителем')
def step_then_game_should_declare_winner(context):
    assert check_win(context.board, context.player) == True