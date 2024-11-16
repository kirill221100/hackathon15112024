
arcana = {0: "Шут", 1: "Маг", 2: "Верховная Жрица", 3: "Императрица", 4: "Император", 5: "Иерофант", 6: "Влюбленные",
          7: "Колесница", 8: "Правосудие", 9: "Отшельник", 10: "Колесо фортуны", 11: "Сила", 12: "Повешенный",
          13: "Смерть", 14: "Умеренность", 15: "Дьявол", 16: "Башня", 17: "Звезда", 18: "Луна", 19: "Солнце",
          20: "Суд", 21: "Мир"}

arcana_interaction = [
        #  Шут  Маг  Жрица Импра Импер Иероф Влюбл Колесн Справ Отшел КолФ Сила Повеш Смерть Умер Дьяв Башня Звезда Луна Солн Суд Мир
        [  0,    2,   0,    3,   -1,   -2,    2,    0,    1,   0,   3,   2,  -1,   -3,   1,  -2,   -3,   3,    -1,   2,   0,  3 ],  # Шут               0
        [  2,    0,   1,    1,    2,   -1,    2,    3,    0,  -1,   2,   1,   0,   -2,   2,   0,   -2,   2,     1,   3,   1,  2 ],  # Маг               1
        [  0,    1,   0,    2,    0,    3,   -1,    0,    2,   3,   2,   1,   2,    1,   2,  -1,   -2,   3,     3,   1,   0,  2 ],  # Жрица             2
        [  3,    1,   2,    0,    2,    1,    3,    1,    0,  -1,   3,   2,  -1,   -2,   3,   1,   -2,   3,     0,   3,   1,  3 ],  # Императрица       3
        [ -1,    2,   0,    2,    0,    0,   -2,    3,    3,   1,   2,   2,  -2,   -3,   1,   2,   -3,   2,     0,   3,   2,  3 ],  # Император         4
        [ -2,   -1,   3,    1,    0,    0,    1,    0,    2,   3,   2,   1,   0,    1,   3,  -2,   -2,   2,     3,   1,   0,  2 ],  # Иерофант          5
        [  2,    2,  -1,    3,   -2,    1,    0,    3,    1,   0,   2,   1,   0,   -1,   2,   0,   -3,   3,     0,   2,   3,  2 ],  # Влюбленные        6
        [  0,    3,   0,    1,    3,    0,    3,    0,    2,   1,   2,   3,   0,   -1,   1,   2,   -2,   3,     1,   3,   1,  3 ],  # Колесница         7
        [  1,    0,   2,    0,    3,    2,    1,    2,    0,   1,   3,   1,  -1,    0,   1,  -1,   -2,   3,     2,   2,   3,  2 ],  # Справедливость    8
        [  0,   -1,   3,   -1,    1,    3,    0,    1,    1,   0,   2,   0,   3,    1,   2,   0,   -2,   2,     3,   1,   1,  2 ],  # Отшельник         9
        [  3,    2,   2,    3,    2,    2,    2,    2,    3,   2,   0,   3,   2,   -1,   3,   1,   -1,   3,     2,   3,   2,  3 ],  # Колесо Фортуны   10
        [  2,    1,   1,    2,    2,    1,    1,    3,    1,   0,   3,   0,   1,    2,   2,   0,   -1,   3,     0,   2,   2,  2 ],  # Сила             11
        [ -1,    0,   2,   -1,   -2,    0,    0,    0,   -1,   3,   2,   1,   0,    2,   1,   0,   -3,   3,     0,   2,   0,  2 ],  # Повешенный       12
        [ -3,   -2,   1,   -2,   -3,    1,   -1,   -1,    0,   1,  -1,   2,   2,    0,   2,  -2,   -1,   2,     1,   3,  -1,  1 ],  # Смерть           13
        [  1,    2,   2,    3,    1,    3,    2,    1,    1,   2,   3,   2,   1,    2,   0,   1,    0,   3,     2,   3,   1,  3 ],  # Умеренность      14
        [ -2,    0,  -1,    1,    2,   -2,    0,    2,   -1,   0,   1,   0,   0,   -2,   1,   0,    0,   3,    -1,   1,   0,  2 ],  # Дьявол           15
        [ -3,   -2,  -2,   -2,   -3,   -2,   -3,   -2,   -2,  -2,  -1,  -1,  -3,   -1,   0,   0,    0,   1,    -2,   1,  -2,  1 ],  # Башня            16
        [  3,    2,   3,    3,    2,    2,    3,    3,    3,   2,   3,   3,   3,    2,   3,   3,    1,   0,     2,   3,   2,  3 ],  # Звезда           17
        [ -1,    1,   3,    0,    0,    3,    0,    1,    2,   3,   2,   0,   0,    1,   2,  -1,   -2,   2,     0,   2,   3,  2 ],  # Луна             18
        [  2,    3,   1,    3,    3,    1,    2,    3,    2,   1,   3,   2,   2,    3,   3,   1,    1,   3,     2,   0,   3,  3 ],  # Солнце           19
        [  0,    1,   0,    1,    2,    0,    3,    1,    3,   1,   2,   2,   0,   -1,   1,   0,   -2,   2,     3,   3,   0,  3 ],  # Суд              20
        [  3,    2,   2,    3,    3,    2,    2,    3,    2,   2,   3,   2,   2,    1,   3,   2,    1,   3,     2,   3,   3,  0 ]   # Мир              21
    ]

def calculate_arcana(day: int, month: int, year: int):
    a = sum(list(map(int, list(f"{day}{month}{year}"))))
    if a > 22:
        return a - 22
    return a

def calculate_compatibility_between_two_people(first_arcana: int, second_arcana: int):
    a = first_arcana + second_arcana
    general_compatibility = a if a <= 22 else a - 22
    b = general_compatibility + first_arcana
    first_perception = b if b <= 22 else b - 22
    c = general_compatibility + second_arcana
    second_perception = c if c <= 22 else c - 22
    d = general_compatibility + first_perception + second_perception
    result = d if d <= 22 else d - 22
    return {'general_compatibility': {'num': general_compatibility, 'name': arcana[general_compatibility]},
            'first_perception': {'num': first_perception, 'name': arcana[first_perception]},
            'second_perception': {'num': second_perception, 'name': arcana[second_perception]},
            'result': {'num': result, 'name': arcana[result]}, 'point_of_compatibility': arcana_interaction[first_arcana][second_arcana]}