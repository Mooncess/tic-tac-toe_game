import unittest
from io import StringIO
from unittest import mock
from unittest.mock import patch

from app.tic_tac_toe import print_board, get_row


class TicTacToeTest(unittest.TestCase):

    def test_print_board(self):
        """
        Тестирование функции print_board,
        которая отвечает за вывод в консоль
        игрового поля
        """
        # Переданная в функцию игровая доска
        board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]

        # Ожидаемый результат
        expected_output = "-------------\n| X | O | X | \n-------------\n| O | X | O | \n-------------\n| X | O | X | \n-------------\n"

        # Перехват реального результата
        captured_output = StringIO()
        with mock.patch("sys.stdout", captured_output):
            print_board(board)

        # Сравнение результатов
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_get_row_valid_input(self):
        """
        Тестирование функции get_row с корректными данными,
        которая возвращает номер строки,
        введеный пользователем.
        """
        with mock.patch("builtins.input", side_effect=["1"]):
            self.assertEqual(get_row("X"), 0)

    def test_get_row_invalid_input(self):
        """
        Тестирование функции get_row с некорректными данными,
        которая возвращает ошибку,
        с просьбой попробовать снова.
        """
        with mock.patch("builtins.input", side_effect=["4", "2"]):
            captured_output = StringIO()
            with mock.patch("sys.stdout", captured_output):
                row = get_row("O")
            self.assertEqual(row, 1)
            expected_output = "Некорректный ввод. Пробуйте снова.\n"
            self.assertEqual(captured_output.getvalue(), expected_output)

    """
    Тестирование функции play_game(),
    которая отвечает за ход игры
    """

    @patch('builtins.input', side_effect=["1", "1", "3", "1", "2", "2", "3", "2", "3", "3", "no"])
    def test_play_game(self, mock_input):
        # Ожидаемый результат
        expected_output = "Player X wins!"

        # Получение реального результата
        with patch('app.tic_tac_toe.print') as mock_print:
            play_game()
        call_args = [args[0] for args, kwargs in mock_print.call_args_list if args]

        # Сравнение результатов
        self.assertEqual(expected_output, [args[0] for args, kwargs in mock_print.call_args_list if args][-1])


if __name__ == "__main__":
    unittest.main()
