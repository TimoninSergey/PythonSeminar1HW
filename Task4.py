"""Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""

def quarter_range(quarter_number):
    if quarter_number == 1:
        print('X ∈ (0; +∞]; Y ∈ (0; +∞]')
    elif quarter_number == 2:
        print('X ∈ (0; -∞]; Y ∈ (0; +∞]')
    elif quarter_number == 3:
        print('X ∈ (0; -∞]; Y ∈ (0; -∞]')
    elif quarter_number == 4:
        print('X ∈ (0; +∞]; Y ∈ (0; -∞]')
    else:
        print('Введите число от 1 до 4')

quat_num = int(input('Введите номер координатной четверти от 1 до 4: '))

quarter_range(quat_num)

