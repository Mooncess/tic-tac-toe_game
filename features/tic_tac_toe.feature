Feature: Tic-Tac-Toe Game Functions

  Scenario: Проверить, выиграл ли игрок
    Given Пустое игровое поле
    When Игрок выполнил условие выигрыша
    Then Игра должна объявить игрока победителем