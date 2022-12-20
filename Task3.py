"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

def quarter_check(numX, numY):
    if numX == 0 or numY == 0:
        print('Введите ненулевые координаты')
    elif numX > 0 and numY > 0:
        print('I координатная четверть')
    elif numX < 0 and numY > 0:
        print('II координатная четверть')
    elif numX < 0 and numY < 0:
        print('III координатная четверть')
    elif numX > 0 and numY < 0:
        print('IV координатная четверть')

numberX = int(input('Введите координату Х, не равную нулю: '))
numberY = int(input('Введите координату Y, не равную нулю: '))

quarter_check(numberX, numberY)