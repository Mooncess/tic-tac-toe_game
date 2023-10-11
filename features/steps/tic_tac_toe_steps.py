from behave import given, when, then
from unittest.mock import patch
from app.tic_tac_toe import check_win,get_col


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


@given('игровая доска')
def step_given_game_board(context):
    context.board = [["X", "O", "O"], ["O", "X", "O"], [" ", " ", "X"]]


@when('игрок выбирает столбец')
def step_when_player_selects_column(context):
    context.column_number = 1


@then('игра должна установить номер этого столбца')
@patch('builtins.input', side_effect=["1"])
def step_then_game_should_return_column_contents(context, mock_input):
    column_contents = get_col(context.board)
    assert column_contents + 1 == context.column_number
