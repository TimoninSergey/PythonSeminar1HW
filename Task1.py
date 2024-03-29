#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

""" Пример:

- 6 -> да
- 7 -> да
- 1 -> нет """

def day_check(number):
    if number == 6:
        return 'Суббота - выходной день'
    elif number == 7:
        return 'Воскресенье - выходной день'
    elif number > 7 or number < 1:
        return 'Такого дня нет, введите номер от 1 до 7'
    else:
        return 'Будний день'

day = int(input('Введите номер дня от 1 до 7: '))

print(day_check(day))