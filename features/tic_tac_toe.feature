Feature: Tic-Tac-Toe Game Functions

  Scenario: Проверить, выиграл ли игрок
    Given Пустое игровое поле
    When Игрок выполнил условие выигрыша
    Then Игра должна объявить игрока победителем

  Scenario: Выбрать столбец на игровом поле
    Given игровая доска
    When игрок выбирает столбец
    Then игра должна установить номер этого столбца

  Scenario: Начать новую игру
    Given законченная игра
    When игрок выбирает начать новую игру
    Then игра начинается заново
