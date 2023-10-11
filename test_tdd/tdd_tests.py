import unittest
from io import StringIO
from unittest import mock

from app.tic_tac_toe import print_board


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


if __name__ == "__main__":
    unittest.main()